# Autonomous Live Improv & Playback Stream (ALIPS)

An Applied AI architecture for fully automated, real-time interactive animated live streaming on YouTube and Twitch. ALIPS fuses **Augusto Boal's Forum Theatre**, **Jonathan Fox's Playback Theatre**, and **Keith Johnstone's Improvisational Systems** with a low-latency neural puppetry and chat perception stack.

---

## 📚 Complete Project Documentation Index

- [**01. Master System Architecture & Pipeline Specification**](file:///Users/akavinash/agy/live-playback-improvised-stream/docs/01_master_architecture.md)
  *End-to-end topology, detailed latency waterfall (274ms local turnaround), and the Double-Latency Feedback Loop.*
- [**02. Critical Blind Spots & Expert Domain Counsel**](file:///Users/akavinash/agy/live-playback-improvised-stream/docs/02_blind_spots_and_expert_counsel.md)
  *The 6 blind spots you didn't know to ask, in-depth counsel across 6 specialized engineering domains, and the upgraded master precision prompt.*
- [**03. Computational Dramaturgy & Participatory Theatre Systems**](file:///Users/akavinash/agy/live-playback-improvised-stream/docs/03_computational_dramaturgy.md)
  *Mathematical formulation of Augusto Boal's Forum Theatre (Joker facilitation, checkpoint rollback, sigmoidal oppressor resistance), Jonathan Fox's Playback Theatre, Keith Johnstone's Status Seesaw, and the closed-loop PID Tension Governor.*
- [**04. Real-Time Animation, Neural Rigging & Audio DSP**](file:///Users/akavinash/agy/live-playback-improvised-stream/docs/04_realtime_animation_and_audio.md)
  *UE5 MetaHuman vs. Live2D comparison, Apple Live Link Face UDP datagram encoding (52 ARKit blendshapes), VTube Studio WebSocket API, and Hann-windowed anti-pop audio barge-in interruption.*
- [**05. Stream Ingestion, Semantic Clustering & Adversarial Safety**](file:///Users/akavinash/agy/live-playback-improvised-stream/docs/05_stream_ingestion_and_safety.md)
  *High-throughput InnerTube streaming, sliding-window Cosine DBSCAN clustering, G2P phonetic acoustic slur filtering, NeMo Guardrails in-character deflection, and pre-TTS egress safety gates.*
- [**06. Mental Models, Architecture Trade-Offs & Project Roadmap**](file:///Users/akavinash/agy/live-playback-improvised-stream/docs/06_roadmap_and_mental_models.md)
  *Systems-thinking mental models, compute allocation trade-offs, 4-phase production delivery roadmap, and real-time observability telemetry.*
- [**07. Minimalist Line Art, Browser Kinematics & Applied Cognitive Aesthetics**](file:///Users/akavinash/agy/live-playback-improvised-stream/docs/07_minimalist_browser_rendering_and_kinematics.md)
  *The Scott McCloud Masking Effect, 12-joint biological Verlet kinematics, Johnstone status postures in 2D vector space, and Server-Sent Events (SSE) telemetry.*

---

## 🎨 Browser-Native Minimalist Vector Stage (`browser_render/`)

- [**`browser_render/index.html`**](file:///Users/akavinash/agy/live-playback-improvised-stream/browser_render/index.html): Real-time procedural HTML5 Canvas line puppetry engine.
- [**`browser_render/server.py`**](file:///Users/akavinash/agy/live-playback-improvised-stream/browser_render/server.py): Zero-dependency HTTP stage server & Server-Sent Events (SSE) telemetry streamer.
- [**`browser_render/headless_recorder.py`**](file:///Users/akavinash/agy/live-playback-improvised-stream/browser_render/headless_recorder.py): OBS Studio Browser Source & Headless Chromium ingestion guide.

## 📁 Codebase Structure

- [`config.py`](file:///Users/akavinash/agy/live-playback-improvised-stream/config.py): Global configuration, latency budgets, and threshold settings (using native dataclasses).
- [`safety/lexical_g2p.py`](file:///Users/akavinash/agy/live-playback-improvised-stream/safety/lexical_g2p.py): Fast Unicode homoglyph normalization, Aho-Corasick keyword scanner, Shannon entropy filter, and G2P phonetic acoustic slur blocker.
- [`perception/clustering.py`](file:///Users/akavinash/agy/live-playback-improvised-stream/perception/clustering.py): Vectorized cosine DBSCAN clustering, medoid extraction, outlier detection, and attention snapshot XML generator.
- [`dramaturgy/governor.py`](file:///Users/akavinash/agy/live-playback-improvised-stream/dramaturgy/governor.py): Closed-loop PID Tension Governor that stabilizes dramatic pacing.
- [`dramaturgy/state_machine.py`](file:///Users/akavinash/agy/live-playback-improvised-stream/dramaturgy/state_machine.py): Theatrical state machine uniting Boal's Forum Theatre (Joker, Oppressor Resistance Sigmoid, Rollback) with Johnstone's Status Seesaw and Re-incorporation Ledger.
- [`audio_rig/barge_in.py`](file:///Users/akavinash/agy/live-playback-improvised-stream/audio_rig/barge_in.py): Low-latency audio barge-in interruption controller with Hann-window cross-fade decay, Apple Live Link Face UDP datagram encoder, and VTube Studio WebSocket injector.
- [`pipeline.py`](file:///Users/akavinash/agy/live-playback-improvised-stream/pipeline.py): Master orchestrator coordinating all subsystems.
- [`main.py`](file:///Users/akavinash/agy/live-playback-improvised-stream/main.py): End-to-end execution simulation script.
- [`requirements.txt`](file:///Users/akavinash/agy/live-playback-improvised-stream/requirements.txt): Production dependencies for deployment.

---

## 🚀 Quickstart & Verification

### 1. Launch the Real-Time Browser Line Puppetry Stage:
```bash
python3 browser_render/server.py
```
*The server automatically picks a random, conflict-free unstandard high port (between 34000 and 49000) and displays the clickable URL directly in your terminal.*

Currently active instance:
👉 **[http://localhost:38365](http://localhost:38365)**

### 2. Run the Full Backend Improv Simulation Harness:
```bash
python3 main.py
```
