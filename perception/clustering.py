"""
Perception Module: Real-time Cosine DBSCAN Semantic Clustering, Medoid Extraction,
and Structured Attention Snapshot Synthesis.
Includes pure NumPy DBSCAN fallback if scikit-learn is not installed.
"""
import numpy as np
from typing import List, Dict, Any, Optional

try:
    from sklearn.cluster import DBSCAN
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

def numpy_dbscan_precomputed(dist_matrix: np.ndarray, eps: float, min_samples: int) -> np.ndarray:
    """
    Vectorized NumPy implementation of DBSCAN for precomputed distance matrices.
    Runs in milliseconds for N <= 1000.
    """
    n_points = dist_matrix.shape[0]
    labels = np.full(n_points, -1, dtype=int)
    cluster_id = 0

    visited = np.zeros(n_points, dtype=bool)

    for i in range(n_points):
        if visited[i]:
            continue
        visited[i] = True

        neighbors = np.where(dist_matrix[i] <= eps)[0]
        if len(neighbors) < min_samples:
            labels[i] = -1
        else:
            labels[i] = cluster_id
            seeds = list(neighbors)
            s_idx = 0
            while s_idx < len(seeds):
                current_point = seeds[s_idx]
                if not visited[current_point]:
                    visited[current_point] = True
                    current_neighbors = np.where(dist_matrix[current_point] <= eps)[0]
                    if len(current_neighbors) >= min_samples:
                        seeds.extend([p for p in current_neighbors if p not in seeds])
                if labels[current_point] == -1:
                    labels[current_point] = cluster_id
                s_idx += 1
            cluster_id += 1

    return labels


class SemanticClusteringPerceptionEngine:
    def __init__(self, intent_prototypes: Dict[str, str], embedding_dim: int = 384):
        self.embedding_dim = embedding_dim
        self.intent_labels = list(intent_prototypes.keys())
        self.intent_texts = list(intent_prototypes.values())
        self.intent_vectors = self._fallback_embed(self.intent_texts)

    def _fallback_embed(self, texts: List[str]) -> np.ndarray:
        vectors = []
        for text in texts:
            words = text.lower().split()
            vec = np.zeros(self.embedding_dim, dtype=np.float32)
            for i, w in enumerate(words):
                h = hash(w) % self.embedding_dim
                vec[h] += 1.0 / (i + 1.0)
            norm = np.linalg.norm(vec)
            if norm > 1e-6:
                vec /= norm
            else:
                vec[0] = 1.0
            vectors.append(vec)
        return np.array(vectors, dtype=np.float32)

    def process_window(
        self,
        comments: List[Dict[str, Any]],
        context_vector: Optional[np.ndarray] = None,
        eps: float = 0.28,
        min_samples: int = 2,
        consensus_threshold: float = 0.12
    ) -> Dict[str, Any]:
        if not comments:
            return {"consensus": [], "outliers": [], "narrative": []}

        texts = [c["text"] for c in comments]
        embeddings = self._fallback_embed(texts)
        n_samples = len(embeddings)

        if context_vector is None:
            context_vector = np.zeros(self.embedding_dim, dtype=np.float32)
            context_vector[0] = 1.0

        # 1. Cosine Distance Matrix via GEMM: D = 1.0 - X * X.T
        similarity_matrix = np.dot(embeddings, embeddings.T)
        dist_matrix = np.clip(1.0 - similarity_matrix, 0.0, 2.0)

        # 2. DBSCAN
        if HAS_SKLEARN:
            db = DBSCAN(eps=eps, min_samples=min_samples, metric="precomputed")
            labels = db.fit_predict(dist_matrix)
        else:
            labels = numpy_dbscan_precomputed(dist_matrix, eps=eps, min_samples=min_samples)

        unique_labels = set(labels)
        consensus_clusters = []
        cluster_centroids = {}

        # 3. Consensus Topics (Medoid Extraction)
        for label in unique_labels:
            if label == -1:
                continue
            indices = np.where(labels == label)[0]
            size = len(indices)
            share = size / n_samples

            cluster_vectors = embeddings[indices]
            centroid = np.mean(cluster_vectors, axis=0)
            norm = np.linalg.norm(centroid)
            if norm > 1e-6:
                centroid /= norm
            cluster_centroids[label] = centroid

            if share >= consensus_threshold:
                dists = 1.0 - np.dot(cluster_vectors, centroid)
                medoid_idx = indices[np.argmin(dists)]

                consensus_clusters.append({
                    "representative_comment": comments[medoid_idx]["text"],
                    "author": comments[medoid_idx].get("author", "viewer"),
                    "share_percent": round(share * 100, 1),
                    "cluster_size": int(size)
                })

        consensus_clusters.sort(key=lambda x: x["cluster_size"], reverse=True)

        # 4. Provocative Outliers (from noise points)
        noise_indices = np.where(labels == -1)[0]
        outlier_candidates = []
        all_centroids = np.array(list(cluster_centroids.values())) if cluster_centroids else None

        for idx in noise_indices:
            comment_text = comments[idx]["text"]
            if len(comment_text) < 12:
                continue

            e = embeddings[idx]
            herd_dist = 1.0 if all_centroids is None else float(np.min(1.0 - np.dot(all_centroids, e)))
            context_novelty = float(1.0 - np.dot(e, context_vector))
            length_factor = min(1.0, len(comment_text) / 35.0)

            score = herd_dist * context_novelty * length_factor
            outlier_candidates.append({
                "comment": comments[idx],
                "novelty_score": round(score, 3)
            })

        outlier_candidates.sort(key=lambda x: x["novelty_score"], reverse=True)
        top_outliers = [c["comment"] for c in outlier_candidates[:2]]

        # 5. Narrative Interventions (Intent Subspace Projection)
        intent_scores = np.dot(embeddings, self.intent_vectors.T)
        max_scores = np.max(intent_scores, axis=1)

        narrative_interventions = []
        for idx, base_score in enumerate(max_scores):
            tier_mult = comments[idx].get("tier_multiplier", 1.0)
            priority = float(base_score * tier_mult)
            if priority >= 0.70:
                matched_label = self.intent_labels[np.argmax(intent_scores[idx])]
                narrative_interventions.append({
                    "action_intent": matched_label,
                    "text": comments[idx]["text"],
                    "author": comments[idx].get("author", "viewer"),
                    "tier_multiplier": tier_mult,
                    "priority_score": round(priority, 3)
                })

        narrative_interventions.sort(key=lambda x: x["priority_score"], reverse=True)

        return {
            "consensus": consensus_clusters[:2],
            "outliers": top_outliers,
            "narrative": narrative_interventions[:3]
        }

    def generate_perception_xml(self, perception_data: Dict[str, Any], total_volume: int) -> str:
        xml_lines = [f'<ambient_chat_perception total_volume="{total_volume}">']

        xml_lines.append('  <consensus_mob_sentiment>')
        for c in perception_data.get("consensus", []):
            xml_lines.append(
                f'    <consensus share="{c["share_percent"]}%" author="{c["author"]}">"{c["representative_comment"]}"</consensus>'
            )
        xml_lines.append('  </consensus_mob_sentiment>')

        xml_lines.append('  <provocative_outliers>')
        for o in perception_data.get("outliers", []):
            xml_lines.append(f'    <outlier author="{o.get("author", "viewer")}">"{o["text"]}"</outlier>')
        xml_lines.append('  </provocative_outliers>')

        xml_lines.append('  <priority_narrative_interventions>')
        for n in perception_data.get("narrative", []):
            xml_lines.append(
                f'    <intervention intent="{n["action_intent"]}" author="{n["author"]}" priority="{n["priority_score"]}">'
                f'"{n["text"]}"</intervention>'
            )
        xml_lines.append('  </priority_narrative_interventions>')

        xml_lines.append('</ambient_chat_perception>')
        return "\n".join(xml_lines)
