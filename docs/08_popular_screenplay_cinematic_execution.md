# Computational Dramaturgy & Cinematic Screenplay Execution
**Architecture Specification 08: Full-Element Screenplay Translation, Procedural Kinematics & Applied AI Foley**

---

## 1. Executive Summary & Dramaturgical Paradigm

Translating iconic screenplays into an autonomous, real-time, participatory browser stage requires bridging **classical dramatic structure** with **computational kinematics and Applied AI audio-visual synthesis**.

Most AI adaptations fail because they treat screenplays merely as raw text to feed into a Text-to-Speech (TTS) engine. In genuine cinematic theatre, **text represents less than 30% of the narrative information**. The remaining 70% resides in:
1. **Status Transactions**: Micro-fluctuations in Keith Johnstone's 1.0–10.0 dominance continuum.
2. **Proxemics & Physical Blocking**: Spatial distance, advances, retreats, cornering, and territorial claiming.
3. **Prop Interactivity**: Physical touchpoints that ground high-stakes tension (e.g., Jules Winnfield biting into a Big Kahuna Burger, sipping Sprite through a straw, opening Marcellus Wallace's glowing briefcase, aiming a 9mm pistol).
4. **Acoustic Texture & Foley**: Instantaneous physical impacts (gunshots, table slams, straw slurps, drum rimshots, cymbal chokes, slaps) synchronized with skeletal kinematics.
5. **Cinematographic Language**: Panning, focal push-ins (establishing two-shot $\rightarrow$ extreme close-up at $2.1\times$), and exponential screen shake decay.

This document details the complete end-to-end implementation of **Quentin Tarantino's *Pulp Fiction* (1994) - "Ezekiel 25:17" Apartment Climax** and **Damien Chazelle's *Whiplash* (2014) - "Not Quite My Tempo"**, alongside the existing suites from *A Few Good Men*, *The Dark Knight*, and *The Social Network*.

---

## 2. Screenplay AST (Abstract Syntax Tree) Data Schema

In `/screenplays/scene_library.py` and `browser_render/index.html`, every screenplay is parsed into an executable, beat-by-beat AST:

```python
{
    "id": 16,
    "speaker": "AGENT_A",
    "dialogue": "And I will strike down upon thee with great vengeance and furious anger...",
    "status_a": 10.0,            # Keith Johnstone Dominance Scale [1.0, 10.0]
    "status_b": 0.8,             # Oppressed character collapse
    "tension": 1.0,              # Global Dramatic Tension T ∈ [0.0, 1.0]
    "target_x_a": 0.58,          # Normalized stage coordinate [0.0, 1.0]
    "target_x_b": 0.68,          # Normalized target coordinate
    "gesture_a": "ROAR_EZEKIEL_CLIMAX",
    "gesture_b": "FLINCH_TERROR",
    "cam_zoom": 2.0,             # Virtual camera magnification factor
    "cam_label": "FURIOUS ANGER CRESCENDO",
    "shake": 1.0,                # Camera trauma amplitude [0.0, 2.0]
    "foley_cues": ["GUNSHOT_EXECUTION", "BURGER_BITE", "STRAW_SLURP"]
}
```

---

## 3. Screenplay Benchmark Analysis

### 3.1 Quentin Tarantino: *Pulp Fiction* (1994) — The Ezekiel 25:17 Apartment Scene
* **Core Dynamic**: The terrifying transition from polite, mundane small talk to explosive Old Testament retribution.
* **Character A**: **JULES WINNFIELD** (Samuel L. Jackson). Righteous, calm, highly articulate, calculating hitman. Status moves from 8.5 (playful predator) to 10.0 (biblical executioner).
* **Character B**: **BRETT** (Frank Whaley). Paralyzed, cornered, terrified college kid. Status collapses from 3.0 down to 0.5.
* **Key Props**:
  - *Dilapidated Wooden Kitchen Table & Chair*: Anchors the interrogation space.
  - *Big Kahuna Burger Box*: Hawaiian burger joint motif with red logo bar.
  - *Fast-Food Cup with Bendy Straw*: Rhythmic prop used to prolong suspense through sound.
  - *The Glowing Golden Briefcase*: The glowing MacGuffin of Marcellus Wallace emitting volumetric radial amber/golden rays (`#fbbf24`).
  - *9mm Pistol & Red Laser Sightline*: Vector firearm drawn at Beat 9, maintaining a laser target onto Brett's head until the execution.
* **Climax**: Verbatim 17-beat recitation of Ezekiel 25:17, culminating in a camera push-in to $2.1\times$, a bright muzzle flash canvas flash, and a low-frequency procedural gunshot boom with 1.4 magnitude camera shake.

### 3.2 Damien Chazelle: *Whiplash* (2014) — "Not Quite My Tempo"
* **Core Dynamic**: Relentless perfectionism, tempo micro-control, and psychological humiliation.
* **Character A**: **TERENCE FLETCHER** (J.K. Simmons). Symphonic conductor, status 10.0, weaponized tempo.
* **Character B**: **ANDREW NEIMAN** (Miles Teller). Obsessed drummer, status deteriorating under interrogation.
* **Key Props**:
  - *Snare Drum on Chrome Tripod*: Physical acoustic instrument with tripod geometry.
  - *Ride Cymbal & Boom Stand*: High-frequency metal resonance surface.
  - *Conductor Music Stand*: Visual divider between instructor and student.
  - *Drumsticks*: In-hand props trembling in Andrew's grip.
* **Audio Interventions**: Drum rimshot on tempo count, cymbal choke on cutoff, and physical slap transient when Fletcher confronts Andrew.

---

## 4. Applied AI Biomechanics & 2-Bone Analytical IK

### 4.1 Inverse Kinematics Formulation
Leg locomotion and arm gestures are driven by an analytical closed-form 2-Bone Inverse Kinematics solver using the **Law of Cosines**:

$$\beta = \arccos\left(\frac{L_1^2 + d^2 - L_2^2}{2 L_1 d}\right)$$

Where:
- $L_1, L_2$ are upper and lower limb segment lengths (e.g. $62\text{px}$ each).
- $d = \text{clamp}(\sqrt{\Delta x^2 + \Delta y^2}, 1.0, 0.999(L_1 + L_2))$ prevents geometric singularities.
- Bend direction is constrained by character facing ($\pm 1$).

### 4.2 In-Hand Dynamic Vector Props
When characters enter specific emotional beats, specialized vector geometry dynamically binds to the hand coordinates $(rHandX, rHandY)$:
1. **The 9mm Firearm**:
   - $20\text{px}$ barrel with trigger guard and grip.
   - Procedural red dashed targeting line ($[4, 4]$ dash pattern) projected across the stage.
   - 8-point geometric muzzle starburst rendered during `GUNSHOT_EXECUTION`.
2. **The Big Kahuna Burger**:
   - Dual-layer amber bun with green lettuce vector held directly to the character's viseme mouth.
3. **The Drink Cup with Straw**:
   - White fast-food container with an angled red straw resting at the mouth plane.
4. **Drumsticks & Conductor Baton**:
   - High-contrast sticks with continuous sinusoidal oscillation during conducting and drum rolls.

---

## 5. Zero-Dependency Web Audio Foley Synthesis Engine

Pre-recorded audio samples introduce bandwidth bloat, CORS issues, and playback latency. The ALIPS engine synthesizes all sound effects **procedurally via the Web Audio API**:

| Foley Sound | Synthesis Algorithm | Acoustical Parameters |
| :--- | :--- | :--- |
| **Gunshot Boom** | Low-frequency sine sweep + shaped noise burst | $160\text{Hz} \rightarrow 28\text{Hz}$ exponential ramp ($0.45\text{s}$) + Biquad lowpass sweep ($6000\text{Hz} \rightarrow 150\text{Hz}$) |
| **Burger Crunch** | Modulated bandpass noise burst | Center $2400\text{Hz}$, $Q = 3.0$, envelope $150\text{ms}$ |
| **Straw Slurp** | Frequency-modulated triangle oscillator | Linear pitch sweep $320\text{Hz} \rightarrow 740\text{Hz} \rightarrow 410\text{Hz}$ |
| **Briefcase Click** | Dual square-wave transient clicks | Double pulses ($0\text{s}, 0.08\text{s}$), $1400\text{Hz} \rightarrow 400\text{Hz}$ exponential decay |
| **Gavel Strike** | Dual-harmonic resonant sine waves | Fundamental $220\text{Hz}$ + overtone $580\text{Hz}$ decaying over $0.25\text{s}$ |
| **Drum Rimshot** | Low triangle body + high transient noise | $340\text{Hz} \rightarrow 60\text{Hz}$ over $120\text{ms}$ with high initial gain |
| **Cymbal Choke** | Highpass filtered Gaussian noise | Highpass cutoff $5500\text{Hz}$, $700\text{ms}$ decay |
| **Binaural Tension Drone** | Continuous sub-bass oscillator | $45\text{Hz} + (T \times 15\text{Hz})$ with gain scaling with $T \in [0.0, 1.0]$ |

---

## 6. Augusto Boal Forum Theatre: Live Spect-Actor Intervention

The engine operationalizes **Augusto Boal's Forum Theatre** by allowing audience members or viewers to halt iconic cinematic scenes and test alternative interrogation tactics:

1. **Scene Freeze**: Clicking `⚡ FORUM STOP! (INTERVENE)` pauses the auto-play timer, halts speech synthesis, and renders the red Forum Theatre intervention border.
2. **Actor Substitution**: The participant selects whether to replace **Character A** (the oppressor) or **Character B** (the target).
3. **Tactical Selection & Text Injection**:
   - *Appease & De-escalate*: Yields status (+0.5) to test if submissiveness reduces violence.
   - *Direct Confrontation*: Surges status (+3.5) to test if mutual defiance forces a stalemate.
   - *Whistleblower / Divine Reason*: Radical status pivot (+4.0) targeting moral dilemmas.
   - *Stoic Silence*: High status holding through non-responsiveness.
4. **Oppressor Resistance Sigmoid ($R_{opp}$)**:
   $$R_{opp}(S_{diff}) = \frac{1}{1 + e^{-k(S_{opp} - S_{user} - \theta)}}$$
   If the user's intervention status overcomes the resistance threshold $\theta$, the oppressor's dominant posture breaks and tension decreases; otherwise, the scene escalates.
5. **Live Vocalization**: The browser's native speech synthesis articulates the user's line with custom actor pitch, before cleanly returning control to the screenplay pipeline.

---

## 7. Verification & Operational Instructions

The cinematic screenplay theater is live and running on the conflict-free high port:
* **Active Port**: Tracked dynamically in `browser_render/active_port.txt` (currently `38365`).
* **Web Stage**: `http://localhost:38365`
* **Real-time Telemetry Stream**: `http://localhost:38365/stream`

To switch between screenplays, select from the top dropdown:
- *Quentin Tarantino: Pulp Fiction (1994) - Ezekiel 25:17* (Default)
- *Aaron Sorkin: A Few Good Men (1992) - "Code Red" Courtroom Climax*
- *Christopher Nolan: The Dark Knight (2008) - Interrogation Room*
- *Damien Chazelle: Whiplash (2014) - "Not Quite My Tempo"*
- *David Fincher: The Social Network (2010) - "Lawyer Up, Asshole"*
- *Autonomous Dramaturgy Engine: The Blackwood Silver (Forum Theatre)*
