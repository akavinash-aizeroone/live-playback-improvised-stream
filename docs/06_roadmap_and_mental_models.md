# 06. Mental Models, Architecture Trade-Offs & Project Roadmap

## Executive Summary

Building an autonomous real-time streaming show requires systems thinking across distributed infrastructure, real-time audio/graphics, and social crowd psychology. This guide establishes the mental models, architectural trade-offs, and phased execution roadmap to scale ALIPS from a local test harness into a 24/7 broadcast-grade production.

---

## 1. Core Mental Models for Applied AI Systems

### 1. The Perceptual Bottleneck (Compression over Concatenation)
- **Anti-Pattern**: Concatenating raw streaming chat into the LLM context window. Leads to context pollution, high latency, and high cost.
- **Mental Model**: Biological perception does not process every photon; it processes high-level sensory abstractions. Use fast feature models (ONNX embeddings + DBSCAN) to compress 500 signals into 3 structured modalities: *Consensus*, *Outliers*, and *Narrative Interventions*.

### 2. The Double-Latency Feedback Loop
- **Anti-Pattern**: Optimizing token generation time while ignoring broadcast egress and client-side player buffering.
- **Mental Model**: Latency is a circuit:
  $$\text{Perceived Lag} = T_{\text{chat\_ingress}} + T_{\text{AI\_turnaround}} + T_{\text{video\_egress}} + T_{\text{player\_buffer}}$$
  YouTube adds 2.5–3.5s on the egress side. Design an **Audience Perception Mask** (instant involuntary micro-reactions within 150ms) to acknowledge the viewer before heavy generative computation finishes.

### 3. Closed-Loop Tension Stabilization vs. Open-Loop Hallucination
- **Anti-Pattern**: Letting LLMs generate free-form improv turns. Causes either rapid narrative exhaustion or surreal divergence.
- **Mental Model**: Narrative pacing is a physical process governed by feedback control. Use a **PID Tension Governor** to measure observed tension error against a target story spine and modulate agent status gaps, tilts, and musical BPM.

### 4. The Anti-Magical Principle (Augusto Boal)
- **Anti-Pattern**: Having an oppressor or antagonist instantly surrender when an audience member suggests a polite or simplistic solution.
- **Mental Model**: Catharsis requires overcoming genuine resistance. Use a sigmoidal oppressor resistance function that demands verifiable leverage and coalition solidarity before granting concessions.

---

## 2. Architecture Trade-Off Decision Matrix

| Dimension | Option A: MetaHuman 3D (Unreal Engine 5) | Option B: Live2D / VRM (VTube Studio / Warudo) | Option C: StreamDiffusion (SD-Turbo) | Recommended Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **Visual Fidelity** | Photorealistic AAA cinematic quality | Stylized 2D/3D anime aesthetic | Real-time generative diffusion | Start with **Option B (Live2D/VRM)** to validate narrative mechanics before scaling to 3D. |
| **GPU / Compute Load** | Heavy (Needs dedicated RTX 4080/4090 for Lumen/Nanite) | Ultra-light (<5% GPU load on standard GPU) | Dedicated 100% GPU utilization on RTX 4090 | **Option B** frees GPU resources for local LLMs and hardware video encoding. |
| **24/7 Broadcast Stability** | Medium (Risk of VRAM leaks or D3D device crashes in long runs) | Extremely high (Battle-tested across thousands of VTubers) | Low (Prone to temporal flicker and hallucinatory drift) | **Option B** provides the highest uptime for automated streams. |
| **Interactivity Protocol** | Apple Live Link UDP (port 11111) | WebSocket JSON-RPC (port 8001) / VMC OSC | Spout2 Shared Texture pointer | Both protocols are implemented in `audio_rig/barge_in.py`. |

---

## 3. Four-Phase Production Delivery Roadmap

```
PHASE 1: Core Perception & Theatrical State Engine (Completed)
├── Fast Lexical, Homoglyph & G2P Phonetic Filters
├── Streaming Cosine DBSCAN Clustering Engine
├── Attention XML Snapshot Builder
├── Johnstone Status Seesaw & Boal Forum State Machine
└── Closed-Loop PID Dramatic Tension Governor

PHASE 2: Ingestion & Live Avatar Hookup (Current Sprint)
├── Deploy Node.js youtubei.js cluster with residential proxy rotation
├── Bind chat output to Redis Streams (chat:general and chat:priority)
├── Connect audio_rig/barge_in.py to Cartesia Sonic WebSocket API
└── Configure VTube Studio (port 8001) or UE5 LiveLink (port 11111)

PHASE 3: Dramaturgical Authoring & Rehearsal
├── Author initial Forum Theatre Anti-Model scenarios (workplace, mystery, crisis)
├── Calibrate Oppressor Resistance weights against red-team audience tests
├── Seed Episodic Re-incorporation Ledgers with platform assets
└── Tune PID Governor coefficients (Kp=0.8, Ki=0.05, Kd=0.15)

PHASE 4: Autonomous Live Broadcast Egress
├── Configure OBS Studio 30+ with Spout2 zero-copy source receiver
├── Set video encoder to NVENC Low-Latency CBR (GOP=60, B-frames=0)
├── Configure YouTube Live Stream Settings to "Ultra-Low Latency"
└── Connect OBS output via SRT Caller Mode with 150ms buffer
```

---

## 4. Key Observability & Telemetry Metrics

To maintain broadcast health, monitor these real-time signals:

1. **E2E Perception Latency**: Time elapsed from Redis Stream pop to XML snapshot generation (Target: $< 35\text{ms}$).
2. **Buffer Lag (Ingest Delta)**: Consumer group lag on incoming chat stream (Target: $< 200\text{ms}$).
3. **P0 Barge-In Latency**: Time from SuperChat arrival to audio buffer flush and neutral face lerp (Target: $< 40\text{ms}$).
4. **PID Pacing Error $e(t)$**: Difference between target tension and observed tension (Target: $|e(t)| < 0.20$).
5. **Pre-TTS Egress Safety Rejection Rate**: Percentage of LLM candidate lines flagged by Llama Guard 3 or phonetic scanner (Target: $< 0.5\%$).
