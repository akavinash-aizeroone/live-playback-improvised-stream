# 03. Computational Dramaturgy & Participatory Theatre Systems

## Executive Summary

Unconstrained LLM improvisation collapses into either repetitive platitudes or surreal nonsense within 15–20 minutes. To maintain narrative coherence, dramatic stakes, and audience catharsis across multi-hour live broadcasts, the system formalizes three foundational traditions of 20th-century participatory and improvisational theatre into distributed agent algorithms:
1. **Augusto Boal's Forum Theatre (Theatre of the Oppressed)**: Anti-model simulation, the Joker meta-facilitator, checkpoint state rollback, and the spect-actor intervention loop guarded by reality-check invariants against magical solutions.
2. **Jonathan Fox & Jo Salas's Playback Theatre**: The Conductor-Teller elicitation pipeline, ritual transformation forms (Fluid Sculptures, Pairs, Stories, Tabloids), and affective musical underscoring as a tempo clock.
3. **Keith Johnstone & Viola Spolin's Improvisational Theatre**: Dynamic status transaction seesaw (1–10 scale), CROW platforming, procedural tilts, and an episodic re-incorporation ledger.

---

## 1. Augusto Boal's Forum Theatre Architecture

```
                  +----------------------------------------------+
                  |           AUDIENCE / SPECT-ACTORS            |
                  +----------------------------------------------+
                           |                              ^
          [Interrupt: "STOP!"]                [Socratic Reflection /
                           |                   Reality Verification]
                           v                              |
             +---------------------------+                |
             |        JOKER AGENT        |----------------+
             | (Meta-Facilitator & Gate) |
             +---------------------------+
               |           |           |
       [Rollback]    [Substitute]   [Anti-Magical Gate]
               |           |           |
               v           v           v
    +-------------------------------------------------------+
    |                     SCENE RUNTIME                     |
    |  +--------------------+       +--------------------+  |
    |  |  SPECT-ACTOR PROXY | <---> |  OPPRESSOR AGENT   |  |
    |  |  (User / Puppet)   |       |  (Adaptive System) |  |
    |  +--------------------+       +--------------------+  |
    |  +--------------------+                               |
    |  |    ALLY AGENTS     |                               |
    |  +--------------------+                               |
    +-------------------------------------------------------+
```

### 1.1 Core Components
- **The Anti-Model**: A scripted or tightly constrained simulation of systemic oppression, interpersonal conflict, or institutional impasse where the Protagonist fails due to flawed tactics or power disparity.
- **The Joker Agent (`JokerGovernor`)**: A neutral, provocative meta-agent. The Joker mediates between audience and fiction, manages the floor, breaks the fourth wall, and halts "magical solutions."
- **The Intervention Loop**: `Run Baseline -> Trigger STOP -> Checkpoint Rollback -> Hot-Swap Protagonist -> Simulate Alternate Tactic -> Evaluate Realism -> Recurse/Debrief`.

### 1.2 Mathematical Oppressor Resistance Model
To prevent cheap, unearned catharsis, the antagonist agent's resistance $R_{opp}(t) \in [0, 1]$ is governed by a logistic sigmoid:
$$R_{opp}(t) = \sigma \left( W_{power} \cdot P_{systemic} - W_{leverage} \cdot L_{tactic}(t) - W_{solidarity} \cdot S_{allies}(t) + \theta_{bias} \right)$$
Where:
- $P_{systemic}$: Institutional power disparity constant ($P \in [0.5, 1.0]$).
- $L_{tactic}(t)$: Calculated legal, evidentiary, or conversational leverage of the spect-actor's offer.
- $S_{allies}(t)$: Active solidarity score contributed by ally agents.
- **Concession Invariant**: The Oppressor yields *only* when $R_{opp}(t) < \tau_{concession}$ (typically $0.25$). Otherwise, it counters, gaslights, or escalates.

---

## 2. Jonathan Fox & Jo Salas's Playback Theatre Architecture

### 2.1 The Conductor-Teller Pipeline
The Conductor interviews an audience member (the Teller) and extracts a formal 4-tuple:
$$\mathcal{T}_{playback} = \langle E_{core}, \mathcal{P}_{dramatis}, T_{pivot}, \mathcal{M}_{poetic} \rangle$$
- $E_{core}$: Core emotional valence and arousal.
- $\mathcal{P}_{dramatis}$: Set of key characters or psychological archetypes.
- $T_{pivot}$: The turning point / irreducible moment of choice.
- $\mathcal{M}_{poetic}$: Extracted non-literal metaphor (e.g., *"A bird trapped behind double glazing"*).

### 2.2 Ritual Enactment Forms
1. **Fluid Sculptures**: Non-linear, 3–4 actors layer repetitive kinetic sounds and metaphor phrases for a singular feeling.
2. **Pairs**: Two actors personify the internal ambivalence or opposing emotional poles of a situation (e.g., "The Pride" vs. "The Terrified Child").
3. **Stories**: Full narrative arc (Setting -> Incident -> Climax -> Shift -> Resolution -> Bow).
4. **Tabloids / Freezes**: Sequential static sculptural snapshots encapsulating distinct thematic chapters.

### 2.3 The Musician as Master Tempo Clock
The Musician agent emits an ambient control vector at 10 Hz:
$$\vec{M}_{audio} = \langle \text{BPM}, \text{HarmonicTension} \in [0, 1], \text{Dynamics} \in [0, 1], \text{Texture} \rangle$$
Actor dialogue turn length is constrained by $\vec{M}_{audio}$: high harmonic tension forces short, breathless sentences; low dynamics enforces hushed physical subtext.

---

## 3. Keith Johnstone & Viola Spolin's Improvisation Engine

### 3.1 The Status Seesaw Engine
Status $S_i(t) \in [1.0, 10.0]$ is negotiated through a dynamic seesaw:
$$\Delta S_i = w_{dom} \cdot \text{Dom}(u_k) - w_{hed} \cdot \text{Hedge}(u_k) + w_{space} \cdot \text{Spatial}(u_k)$$
$$S_j(t+1) = \text{clip}\left(S_j(t) - \alpha \cdot \Delta S_i, 1.0, 10.0\right)$$
- **High Status ($S \ge 7$)**: Relaxed response latency, unbroken eye gaze, imperative syntax, stillness.
- **Low Status ($S \le 4$)**: Instantaneous anxious blurts, excessive qualifiers, nervous laughter, yielding physical space.

### 3.2 The Platform (CROW) & Procedural Tilt
1. **Platform Tracker**: Measures CROW completeness score $C_{crow} = \frac{1}{4}(\mathbb{I}_{Char} + \mathbb{I}_{Rel} + \mathbb{I}_{Obj} + \mathbb{I}_{Where})$.
2. **Procedural Tilt**: When $C_{crow} == 1.0$ for $> 3$ consecutive turns, the scene engine injects a tilt directive to shatter equilibrium without denying established facts.

### 3.3 The Episodic Re-incorporation Ledger
The system logs every introduced entity into a ledger:
```json
[
  {"entity": "Silver Spoon", "category": "PROP", "turn": 1, "resolved": false},
  {"entity": "Oath of St. Jude", "category": "VOW", "turn": 1, "resolved": false}
]
```
During Climax and Resolution beats, token generation is conditioned on closing dangling ledger items rather than inventing new elements.

---

## 4. Closed-Loop PID Dramatic Tension Governor

```
                       +-------------------------------+
                       | TARGET TENSION CURVE T*(t)    |
                       | (Freytag's Pyramid / Spine)   |
                       +-------------------------------+
                                       |
                                       v
 [Observed Tension T(t)] ----> [ ERROR e(t) ] <----+
                                       |            |
                                       v            |
                       +-----------------------+    |
                       |    PID CONTROLLER     |    |
                       | K_p*e + K_i*∫e + K_d*ė|    |
                       +-----------------------+    |
                                   |                |
                       [Pacing Control Vector u(t)] |
                                   |                |
          +------------------------+----------------+-------+
          |                        |                        |
          v                        v                        v
+--------------------+   +--------------------+   +--------------------+
|  INJECT OBSTACLE   |   |   ALTER STATUS     |   |  MODULATE MUSICIAN |
| (If T(t) < T*(t))  |   |     GAP DELTA      |   | (Tempo & Dynamics) |
+--------------------+   +--------------------+   +--------------------+
```

Dramatic tension $T(t) \in [0, 1]$ is computed at each turn:
$$T(t) = w_1 \cdot |S_A(t) - S_B(t)| + w_2 \cdot \Phi_{conflict}(t) + w_3 \cdot \Omega_{urgency}(t) + w_4 \cdot \vec{M}_{tension}(t)$$
The governor adjusts pacing via:
$$u(t) = K_p \, e(t) + K_i \int_0^t e(\tau)\, d\tau + K_d \, \frac{de(t)}{dt}$$
- **$u(t) > 0.25$ (Under-tension)**: Injects relational tilt, status clash, or increases BPM.
- **$u(t) < -0.25$ (Over-tension / Fatigue)**: Injects comic relief, somatic pauses, or sustained harmonic resolution.
