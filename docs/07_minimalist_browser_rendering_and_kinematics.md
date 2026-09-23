# 07. Minimalist Line Art, Browser Kinematics & Applied Cognitive Aesthetics

## Executive Summary

Pivoting from high-overhead 3D rigs (Unreal Engine MetaHumans) to **browser-native minimalist line-art and kinematic stick figures** is both a technical breakthrough and a dramaturgical triumph. 

By running procedural vector rendering directly on the browser client via HTML5 Canvas and Server-Sent Events (SSE) / WebSockets:
1. **Server GPU Compute is Dropped to Zero**: The backend server is relieved of all 3D rendering overhead, dedicating 100% of its silicon to LLM generation, real-time DBSCAN chat perception, and audio synthesis.
2. **Infinite Frame Rate & Zero Bandwidth**: The canvas renders locally at 60–120 FPS on any phone or laptop, consuming only a tiny $5–15\text{ KB/s}$ telemetry stream.
3. **Amplification Through Simplification**: Eliminates the *Uncanny Valley* entirely, inviting audience members to project their own empathy, identity, and emotions onto expressive, organic lines.

---

## 1. Cognitive Science: The Scott McCloud "Masking Effect"

```
+--------------------------------------------------------------------------+
|                       THE ABSTRACTION SPECTRUM                           |
|                                                                          |
|   PHOTOREALISTIC 3D                   EXPRESSIVE LINE ART                |
|   (Unreal MetaHuman)                  (Minimalist Vectors)               |
|   ------------------                  --------------------               |
|   • High specificity                  • Universal identification         |
|   • Viewer sees "ANOTHER PERSON"      • Viewer sees "THEMSELVES"         |
|   • High risk of Uncanny Valley       • Zero uncanny valley              |
|   • Severe GPU compute overhead       • Zero server GPU overhead         |
|   • Fixed age, race, appearance       • Pure archetype of human state    |
+--------------------------------------------------------------------------+
```

In *Understanding Comics*, theorist Scott McCloud introduced the concept of **Amplification Through Simplification**:
- When drawing a human face with hyper-detail, the viewer's brain scrutinizes physical identity, facial flaws, and micro-expressions. Any synthetic flaw triggers the uncanny valley.
- When abstracting a human down to simple expressive lines (a circle for a head, dynamic spine curves, minimal facial slits), the representation shifts from *realistic representation* to a **universal conceptual icon**.
- Because the drawing lacks specific individual features, audience members instinctively project their own psyche into the character. In participatory theatre forms like **Jonathan Fox's Playback Theatre**, this abstraction magnifies empathic connection: a viewer sees their own grief or joy mirrored without the distraction of an avatar's physical specificity.

---

## 2. Mathematical Kinematics & Expressive Lines

A static stick figure feels dead and mechanical. The ALIPS browser engine implements **procedural biological kinematics**:

```
                       [ HEAD ] (Radius: 24px, Dynamic Tilt θ_head)
                          |
                      [ NECK ]
                     /    |    \
           [L_SHOULDER]   |   [R_SHOULDER]
               |       [SPINE] (Curvature Beziers)
            [ELBOW]       |
               |       [PELVIS] (Root position P_x, P_y)
            [HAND]     /      \
                   [L_HIP]    [R_HIP]
                      |          |
                   [KNEE]     [KNEE]
                      |          |
                   [FOOT]     [FOOT] (Ground Horizon)
```

### 2.1 Keith Johnstone Status Postures in 2D Vector Space
The character rig maps Johnstone's Status Scale ($S \in [1.0, 10.0]$) to skeletal geometry:

| Parameter | Dominant / High Status ($S \ge 8$) | Submissive / Low Status ($S \le 3$) |
| :--- | :--- | :--- |
| **Spine Curvature $\theta_{spine}$** | $0^\circ$ (Vertical, proud posture) | $+15^\circ$ forward slump (sagging vertebrae) |
| **Head Angle $\theta_{head}$** | $+5^\circ$ (Looking slightly upward/outward) | $-15^\circ$ (Eyes cast down to ground) |
| **Pelvis Height $Y_{pelvis}$** | Elevated ($+15\text{px}$ taller stance) | Lowered ($-15\text{px}$, knees bent) |
| **Stance Width** | Wide, immovable ($45\text{px}$ base) | Narrow, precarious ($25\text{px}$ base) |
| **Stroke Width** | Assertive, bold ($4.5\text{px}$ line weight) | Delicate, fragile ($2.0\text{px}$ line weight) |
| **Line Stability** | Crisp, still, zero tremor | High-frequency Perlin jitter (anxious trembling) |

### 2.2 Biological Micro-Oscillations
To maintain organic vitality, the characters never freeze:
- **Respiration**: The pelvis and shoulders oscillate vertically:
  $$\Delta Y_{breath} = A_{breath} \cdot \sin(2\pi \cdot f_{breath} \cdot t)$$
  Where $f_{breath} = 0.30 + 0.40 \cdot T(t)\text{ Hz}$ (breathing quickens as dramatic tension $T(t)$ rises).
- **Organic Hand-Drawn Wobble**: Stroke vertices are dynamically displaced by noise scaled by tension:
  $$\mathbf{p}_{render} = \mathbf{p}_{joint} + \vec{n} \cdot \text{RandomJitter} \cdot (1.0 + 1.5 \cdot T(t)) \cdot W_{wobble}$$
  In calm dialogue, lines are smooth and flowing; during heated arguments, lines become raw, agitated, and kinetic.

---

## 3. Two-Way Architecture: Server to Browser

```
+-------------------------------------------------------------------+
|                     ALIPS PYTHON BACKEND                          |
|                                                                   |
|   [Chat Ingestion] ──► [Perception] ──► [Dramaturgy & Tension]    |
|   (InnerTube/Redis)   (Cosine DBSCAN)   (PID Governor & Boal HFSM)|
+-------------------------------------------------------------------+
                                  │
                  (Lightweight JSON Telemetry: 10 Hz)
                  HTTP GET /stream (Server-Sent Events)
                                  │
                                  ▼
+-------------------------------------------------------------------+
|                  BROWSER HTML5 CANVAS CLIENT                      |
|                     (http://localhost:8080)                       |
|                                                                   |
|   • Receives: Tension, Status A/B, Active Speaker, Subtitles     |
|   • Interpolates smoothly at 60 FPS / 120 FPS                    |
|   • Evaluates biological breathing & dynamic line jitter         |
|   • Renders 12-joint expressive line characters natively         |
+-------------------------------------------------------------------+
                                  │
                     (OBS Browser Source Capture)
                                  │
                                  ▼
+-------------------------------------------------------------------+
|                        BROADCAST EGRESS                           |
|       OBS Studio ──(NVENC H.264 / SRT Caller)──► YouTube Live     |
+-------------------------------------------------------------------+
```

---

## 4. Staging Augusto Boal & Jonathan Fox in 2D Minimalist Space

1. **Augusto Boal's Forum Theatre "STOP!" Intervention**:
   - When a spect-actor intervenes, the browser engine halts character kinetic updates immediately.
   - The background tints into an alerting crimson red (`rgba(239, 68, 68, 0.06)`).
   - A crisp rectangular frame locks around the stage with an intervention banner:
     > `⚡ FORUM THEATRE: SPECT-ACTOR INTERVENTION (SCENE HALTED) ⚡`
   - The pre-crisis checkpoint state is held visually frozen while the audience votes on the substitute tactic.
2. **Jonathan Fox's Playback Theatre Pairs & Fluid Sculptures**:
   - In *Pairs*, Agent A and Agent B stand on opposite sides of the horizon line, physically personifying the conflicting emotional poles of the Teller's story.
   - As one agent speaks the Teller's conscious thought, the other's line weight dims and hunches downward; as the shadow emotion speaks, the status see-saw reverses instantly.

---

## 5. Deployment & Streaming Setup

### Option A: Local Broadcast with OBS Studio (Zero Complexity)
1. Launch the stage server:
   ```bash
   python3 browser_render/server.py
   ```
2. Open OBS Studio $\to$ Add Source $\to$ **Browser Source**:
   - **URL**: `http://localhost:8080`
   - **Width**: `1920`
   - **Height**: `1080`
   - **FPS**: `60`
   - Check *"Control audio via OBS"* (if Web Audio is enabled).
3. Click **Start Streaming** in OBS to broadcast to YouTube.

### Option B: Cloud Server Headless Deployment
For running in a headless Linux cloud container (AWS/GCP/Hetzner):
```bash
# Launch virtual display and stage server
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99
python3 browser_render/server.py &

# Ingest via Headless Chromium & FFmpeg pipe to YouTube
node browser_render/headless_recorder.js | ffmpeg -y \
  -f rawvideo -pix_fmt rgba -s 1920x1080 -r 60 -i - \
  -c:v h264_nvenc -b:v 4500k -f flv rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}
```
