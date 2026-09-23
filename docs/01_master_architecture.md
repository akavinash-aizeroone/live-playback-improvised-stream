# 01. Master System Architecture & Pipeline Specification

## Executive Summary

The **Autonomous Live Improv & Playback Stream (ALIPS)** is an Applied AI system designed for fully automated, real-time interactive animated streaming on YouTube and Twitch. It unites the structural rigor of participatory theatre (**Augusto Boal's Forum Theatre**, **Jonathan Fox's Playback Theatre**, and **Keith Johnstone's Improvisational Theatre**) with a modern, low-latency AI broadcast pipeline.

---

## High-Level Topology Diagram

```
                                  LIVE YOUTUBE STREAM
                                           │
         ┌─────────────────────────────────┴─────────────────────────────────┐
         ▼                                                                   ▼
[InnerTube Stream Worker Pool]                                    [YouTube Data API v3 Fallback]
 (youtubei.js / HTTP/2 Chunked)                                     (gRPC / Quota Multiplier)
         │                                                                   │
         └─────────────────────────────────┬─────────────────────────────────┘
                                           ▼
                           [Redis Streams / Ingestion Queue]
                                           │
                                           ▼
                 ┌──────────────────────────────────────────────────┐
                 │    STAGE 0 & 1: PRE-EMBEDDING FAST FILTER        │
                 │ ──────────────────────────────────────────────── │
                 │ 1. Sliding LRU Deduplication Filter              │
                 │ 2. NFKD Unicode + Homoglyph Normalizer           │
                 │ 3. Aho-Corasick Multi-Pattern Prohibited Trie    │
                 │ 4. Shannon Entropy Filter (Spam & Emote Strip)   │
                 │ 5. G2P Phonetic Acoustic Checker (ARPAbet/Lev)   │
                 └─────────────────────────┬────────────────────────┘
                                           │ (Sanitized Text Stream)
                                           ▼
                 ┌──────────────────────────────────────────────────┐
                 │ STAGE 2: SLIDING-WINDOW SEMANTIC CLUSTERING (2s) │
                 │ ──────────────────────────────────────────────── │
                 │ 1. Fast Cosine Distance Matrix GEMM (500x500)    │
                 │ 2. Precomputed Cosine DBSCAN (eps=0.28, min=2)   │
                 │ 3. Tri-Part Attention Snapshot:                  │
                 │    ├─ Consensus: Max-size clusters -> Medoid     │
                 │    ├─ Outlier: Noise points x Novelty x Contrast │
                 │    └─ Narrative: Dot-prod with Action Prototypes │
                 └─────────────────────────┬────────────────────────┘
                                           │ (Compressed XML Perception Snapshot)
                                           ▼
                 ┌──────────────────────────────────────────────────┐
                 │      STAGE 3: THEATRICAL DRAMATURGY ENGINE       │
                 │ ──────────────────────────────────────────────── │
                 │ 1. Johnstone Status Seesaw (1.0 to 10.0 scale)   │
                 │ 2. Closed-Loop PID Tension Governor (Anti-Fatigue)│
                 │ 3. Boal Forum Theatre (Joker Halt & Rollback)    │
                 │ 4. Episodic Re-incorporation Ledger              │
                 └─────────────────────────┬────────────────────────┘
                                           │ (Character Actions & Spoken Dialogue)
                                           ▼
                 ┌──────────────────────────────────────────────────┐
                 │    STAGE 4: AUDIO DSP & RIGGING INTERRUPTIBILITY │
                 │ ──────────────────────────────────────────────── │
                 │ 1. Streaming TTS (Cartesia / ElevenLabs WS)      │
                 │ 2. Hann-Window Cosine Anti-Pop Audio Buffer      │
                 │ 3. LiveLink Face UDP (52 ARKit Blendshapes)      │
                 │ 4. VTube Studio WebSocket (Live2D Injection)     │
                 │ 5. Spout2 / OBS Studio Broadcast Egress          │
                 └──────────────────────────────────────────────────┘
```

---

## Detailed Latency Waterfall & Budgeting

| Pipeline Stage | Sub-Component / Technology | Cloud Baseline | SOTA Optimized | Key Engineering Optimization |
| :--- | :--- | :--- | :--- | :--- |
| **1. Chat Ingestion** | YouTube Live Chat / Twitch EventSub | 250ms – 1,000ms | **50ms – 150ms** | InnerTube chunked HTTP/2 worker pool bypassing 1s poll rate. |
| **2. Fast Filtering** | Lexical + G2P Phonetic + Entropy | 80ms – 150ms | **5ms – 15ms** | Aho-Corasick $O(N)$ matching + Shannon entropy calculation. |
| **3. Embedding & DBSCAN** | BGE-small ONNX + Cosine GEMM | 150ms – 300ms | **15ms – 35ms** | Precomputed BLAS matrix multiplication on unit vectors. |
| **4. LLM Generation** | Groq LPU / vLLM FP8 on RTX 4090 | 350ms – 700ms | **60ms – 140ms** | Speculative decoding + continuous batching. |
| **5. Sentence Chunking** | Clause punctuation / conjunction | 400ms – 800ms | **80ms – 180ms** | Emit first chunk on 4–6 words or comma; never wait for period. |
| **6. Streaming TTS** | Cartesia Sonic WebSocket | 200ms – 350ms | **40ms – 90ms** | Persistent WebSocket connection streaming raw PCM s16le. |
| **7. Blendshape Driving** | NVIDIA Audio2Face / Live Link UDP | 45ms – 80ms | **15ms – 35ms** | Headless microservice driving 52 ARKit float parameters. |
| **8. Frame Compositing** | Spout2 DirectX Zero-Copy to OBS | 30ms – 60ms | **1ms – 5ms** | Shared GPU texture memory bypassing CPU/RAM roundtrips. |
| **9. Hardware Encoder** | OBS NVENC H.264 / AV1 Low Latency | 25ms – 45ms | **8ms – 15ms** | GOP=60 (1s), B-frames=0, low-latency CBR tuning. |
| **Subtotal (Local Loop)**| **Ingress to Encoder Output** | **1,530ms – 3,585ms** | **274ms – 665ms** | Local turnaround executes under 500ms. |
| **10. Platform Egress** | SRT Caller Mode vs. RTMP | 1,000ms – 2,500ms | **150ms – 400ms** | SRT caller with 150ms buffer to YouTube ingest. |
| **11. Player Playback Buffer** | YouTube Ultra-Low Latency (LL-DASH) | 2,000ms – 4,500ms | **1,500ms – 2,500ms** | Hard client-side playback buffer floor on player. |
| **Total Interactivity Loop**| **Viewer Enter $\to$ Voice Heard** | **4,530ms – 10,585ms** | **1,924ms – 3,565ms** | Optimal conversational timing achieved on YouTube. |

---

## The Double-Latency Feedback Loop

In interactive live broadcasting, user experience is governed by the **Double-Latency Feedback Loop**:
$$\text{Total Perceived Latency} = T_{\text{chat\_ingress}} + T_{\text{AI\_turnaround}} + T_{\text{broadcast\_egress}} + T_{\text{player\_buffer}}$$

Because YouTube's player buffer adds 2.0 to 3.5 seconds of non-negotiable delay, the system uses an **Audience Perception Mask**:
1. Within 150ms of comment selection, the avatar triggers an involuntary micro-reaction (eye glance toward the chat monitor, an eyebrow twitch, or an acoustic pause).
2. The viewer perceives that they have been noticed immediately, masking the time required for LLM reasoning and video delivery.
