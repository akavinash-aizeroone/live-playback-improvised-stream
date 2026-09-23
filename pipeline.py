"""
Master Orchestration Engine: Autonomous Live Improv Stream
Glues Ingestion, Safety Sanitization, Semantic Clustering Perception,
Theatrical Dramaturgy Governors, and Audio/Rigging into an automated loop.
"""
import time
from typing import List, Dict, Any

from config import SafetyConfig, PerceptionConfig, DramaturgyConfig, AudioRigConfig
from safety.lexical_g2p import FastLexicalSanitizer, PhoneticAcousticGuard
from perception.clustering import SemanticClusteringPerceptionEngine
from dramaturgy.governor import PIDTensionGovernor
from dramaturgy.state_machine import JohnstoneStatusSeesaw, ReincorporationLedger, BoalForumGovernor
from audio_rig.barge_in import AudioBargeInController, LiveLinkFaceEncoder, VTubeStudioJsonRPC
from observability import logged

class AutonomousImprovStreamOrchestrator:
    def __init__(self):
        # Initialize configurations
        self.safety_cfg = SafetyConfig()
        self.perception_cfg = PerceptionConfig()
        self.dramaturgy_cfg = DramaturgyConfig()
        self.audio_cfg = AudioRigConfig()

        # Initialize sub-engines
        self.sanitizer = FastLexicalSanitizer(self.safety_cfg.banned_keywords)
        self.phonetic_guard = PhoneticAcousticGuard(self.safety_cfg.banned_phonetic_signatures)
        self.perception_engine = SemanticClusteringPerceptionEngine(self.perception_cfg.intent_prototypes)
        self.tension_governor = PIDTensionGovernor(
            kp=self.dramaturgy_cfg.pid_kp,
            ki=self.dramaturgy_cfg.pid_ki,
            kd=self.dramaturgy_cfg.pid_kd,
            setpoint=self.dramaturgy_cfg.target_tension_default
        )
        self.status_seesaw = JohnstoneStatusSeesaw(initial_status_a=7.0, initial_status_b=3.0)
        self.reincorporation = ReincorporationLedger()
        self.boal_governor = BoalForumGovernor(
            systemic_power=self.dramaturgy_cfg.oppressor_power_systemic,
            concession_threshold=self.dramaturgy_cfg.oppressor_concession_threshold
        )
        self.audio_controller = AudioBargeInController(
            sample_rate=self.audio_cfg.sample_rate,
            fade_ms=self.audio_cfg.hann_fade_duration_ms
        )

        # Seed Platform elements
        self.reincorporation.record_element("Grand Duke's Silver Spoon", "PROP", introduced_turn=1)
        self.reincorporation.record_element("The Secret Oath of St. Jude", "VOW", introduced_turn=1)

    @logged(event="pipeline_process_chat_batch", service="stream-pipeline")
    def process_chat_batch(self, raw_comments: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        1. Multi-Stage Fast Sanitization
        2. Semantic Cosine DBSCAN Clustering
        3. Formatted Attention Snapshot Generation
        """
        sanitized_comments = []
        for c in raw_comments:
            text = c.get("text", "")
            is_clean, clean_or_reason = self.sanitizer.filter_text(text)
            if not is_clean:
                continue

            # Phonetic acoustic safety check
            is_safe, _ = self.phonetic_guard.scan(clean_or_reason)
            if not is_safe:
                continue

            sanitized_comments.append({
                "author": c.get("author", "viewer"),
                "text": clean_or_reason,
                "tier_multiplier": c.get("tier_multiplier", 1.0)
            })

        # Process sliding window clustering
        perception_snapshot = self.perception_engine.process_window(
            sanitized_comments,
            eps=self.perception_cfg.dbscan_eps,
            min_samples=self.perception_cfg.dbscan_min_samples
        )
        xml_snapshot = self.perception_engine.generate_perception_xml(perception_snapshot, len(raw_comments))

        return {
            "sanitized_count": len(sanitized_comments),
            "snapshot_data": perception_snapshot,
            "perception_xml": xml_snapshot
        }

    @logged(event="pipeline_dramaturgical_tick", service="stream-pipeline")
    def run_dramaturgical_tick(self, observed_tension: float, speaker: str, status_move: str) -> Dict[str, Any]:
        """
        Evaluates dramatic pacing via PID tension governor and updates Johnstone status balance.
        """
        pacing_result = self.tension_governor.update(observed_tension)
        status_result = self.status_seesaw.apply_transaction(speaker, status_move)
        dangling_callbacks = self.reincorporation.get_dangling_elements()

        return {
            "pacing": pacing_result,
            "status_distribution": status_result,
            "dangling_callbacks": dangling_callbacks
        }

    @logged(event="pipeline_simulate_barge_in", service="stream-pipeline")
    def simulate_barge_in(self, high_priority_event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handles P0 SuperChat or raid event:
        Cuts audio with anti-pop cosine fade, resets face blendshapes to neutral,
        and logs the interruption event.
        """
        anti_pop_tail = self.audio_controller.execute_barge_in_cut()
        neutral_frame = LiveLinkFaceEncoder.encode_frame("MetaHuman_Actor", {})
        live2d_neutral = VTubeStudioJsonRPC.make_mouth_frame(mouth_open=0.0, mouth_smile=0.2)

        return {
            "barge_in_triggered": True,
            "tail_bytes": len(anti_pop_tail),
            "livelink_packet_bytes": len(neutral_frame),
            "vtube_studio_payload": live2d_neutral,
            "event": high_priority_event
        }
