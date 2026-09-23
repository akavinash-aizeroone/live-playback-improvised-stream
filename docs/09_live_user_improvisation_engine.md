# Live Story Improvisation Engine & Theatrical Dialogue Injection
**Architecture Specification 09: Applied AI Audience Word Ingestion, Keith Johnstone Offers & Real-Time Beat Splicing**

---

## 1. Executive Summary & Applied AI Theatrical Mechanics

In traditional improvisational theatre (Keith Johnstone, Viola Spolin, Del Close), scenes do not advance through arbitrary random words; they advance through a formal structural dialectic known as **Offers, Tilts, and Re-incorporation**:

1. **The Offer**: An audience member or actor introduces a concrete physical object, relationship reveal, or environmental shock (e.g. *"poisoned coffee"*, *"I am your brother"*, *"stolen diamond"*, *"FBI wiretap"*).
2. **Acceptance ("Yes, and...")**: The active character never rejects or denies the offer ("blocking"). Instead, they accept the reality of the offer and add new stakes to it.
3. **The Tilt**: The offer creates an immediate status inversion or moral dilemma, forcing the characters to reassess their objectives.
4. **Re-incorporation**: The offer is not abandoned after one line; it becomes woven into the dramatic climax.

This module implements a **Live Story Improvisation Director Bar** embedded directly into the browser stage. It enables the user to inject arbitrary words, secrets, or plot twists in real time, causing the autonomous screenplay engine to dynamically generate new theatrical beats, splice them into the active timeline, vocalize them with character-tailored pitch and cadence, drive 2-bone IK gestures, trigger procedural Foley sound synthesis, and modulate 2D cinematographic camera angles.

---

## 2. System Architecture & Dual-Tier Generation Pipeline

The improvisation engine employs a **dual-tier fail-safe architecture** to guarantee zero-latency execution:

```
[ User Input / Audience Chip ]
             │
             ▼
    ┌─────────────────┐
    │ Frontend Client │ ──> Fast HTTP POST ──> [ Python Backend: /api/improvise ]
    │  (index.html)   │ <── Improv Beats JSON <──  (AppliedAIImprovGenerator)
    └─────────────────┘
             │
      (Network Fallback)
             ▼
   [ Client-Side Engine ]
 (generateClientImprovBeats)
             │
             ▼
 ┌────────────────────────────────────────────────────────┐
 │ 1. Spliced into SCREENPLAYS[active].beats              │
 │ 2. Immediate applyBeat(currentBeatIndex + 1)           │
 │ 3. Native Web Speech API Vocalization                  │
 │ 4. 2-Bone IK Biomechanical Arm & Leg Posing           │
 │ 5. Procedural Foley Sound Trigger (Gun/Table/Slam)     │
 │ 6. Procedural 2D Camera Push-in & Trauma Shake         │
 └────────────────────────────────────────────────────────┘
```

---

## 3. Screenplay Contextual Adaptation Matrix

When an improv word is submitted, the engine transforms the word into character-specific theatrical prose matching each screenplay's distinct rhetorical style:

| Screenplay | Speaker A Adaptation (Lead/Oppressor) | Speaker B Adaptation (Target/Counter-move) | Staging & Foley Trigger |
| :--- | :--- | :--- | :--- |
| **Pulp Fiction** | *"Hold on a second. Did you just say '{word}'?! Vincent, look at me. Did this boy just bring up '{word}'?!"* | *"Jules, I swear on my life! Marcellus Wallace told us the '{word}' was already taken care of in the cupboard!"* | Jules draws 9mm pistol with laser sightline, camera pushes to $1.9\times$, shake $0.7$, climax triggers $2.1\times$ execution. |
| **A Few Good Men** | *"Colonel Jessep, isn't it true that '{word}' was the exact pretext used to authorize the transfer order?"* | *"You sit there in your crisp whites and lecture me about '{word}'?! '{word}' saved lives at Windward Point!"* | Kaffee strides forward with legal pad; Jessep roars with status surge to 10.0, shake $0.9$. |
| **The Dark Knight** | *"Where did you hide the '{word}'?! Tell me!"* | *"You see, Batman... to them, '{word}' is just another bad joke waiting to tear through their civilized order!"* | Batman slams steel interrogation table with procedural sawtooth Foley ($140\text{Hz} \rightarrow 20\text{Hz}$); Joker leans in with philosophical cackle. |
| **Whiplash** | *"Stop! You think '{word}' excuses you dragging four beats behind my tempo?!"* | *"It wasn't '{word}', Mr. Fletcher! I was playing on tempo until my hands bled!"* | Fletcher halts studio rehearsal with cymbal choke, leans into Andrew's face; Andrew tenses drumsticks in trembling grip. |
| **The Social Network** | *"You told Peter Thiel that '{word}' was my responsibility while you diluted my equity to zero!"* | *"The '{word}' didn't scale, Eduardo. Facebook is moving at light speed, and your '{word}' was left in Boston."* | Eduardo slams standing desk with table slam Foley; Mark delivers cold monotone glare. |

---

## 4. UI/UX Interaction Design

The browser stage features a dedicated director interface docked directly above the transport controls:

1. **Text Input Field (`#improv-word-input`)**:
   - Accommodates single words, complex phrases, or full plot twists (e.g. *"armed detonator"*, *"the poison is in the water supply"*, *"he is your biological father"*).
   - Listens to both the `🚀 IMPROVISE NOW` button and the keyboard `Enter` key.
2. **Instant Theatrical Chip Bar (`.chip`)**:
   - Click-to-improvise quick chips:
     - `☕ Poisoned Coffee`
     - `💍 Stolen Diamond`
     - `🩸 Secret Brother`
     - `👽 Alien Secret`
     - `🚨 FBI Wiretap`
     - `💣 Detonator`
3. **Director Intensity Selector (`#improv-intensity`)**:
   - `💥 Narrative Tilt (Dramatic Twist)`: Surges tension by $+0.25$ and triggers a status reversal.
   - `🤝 "Yes, and..." (Subtle Weave)`: Maintains conversational rhythm while weaving in the object.
   - `🔥 Full Disruption (Chaos Climax)`: Immediately elevates tension to $1.0$, triggers camera shake $>1.0$, and initiates an explosive confrontation.
4. **Director Toast Notification (`#director-toast`)**:
   - A floating, neon-cyan glassmorphic notification banner appears in the upper right corner displaying: `🎭 Improvising Story with: "[WORD]"...`.

---

## 5. Algorithmic Beat Splicing & Pacing Stabilization

When new beats are generated, they must not overwrite future scripted beats; they are **spliced non-destructively** into the active screenplay array:

```javascript
// Non-destructive AST beat splicing
sp.beats.splice(currentBeatIndex + 1, 0, ...newBeats);

// Immediate execution of the newly improvised beat
applyBeat(currentBeatIndex + 1);
```

### PID Tension Governor Integration
When an improvised tilt is executed, the dramatic tension $T$ jumps instantaneously. The backend PID Tension Governor (`dramaturgy/governor.py`) dynamically computes the error between current tension and the target pacing setpoint ($T_{target} = 0.70$):

$$e(t) = T_{target} - T_{observed}(t)$$
$$u(t) = K_p e(t) + K_i \int_0^t e(\tau)d\tau + K_d \frac{de(t)}{dt}$$

If the user introduces an explosive tilt that spikes tension to $1.0$, the governor instructs subsequent beats to hold silence, slow down vocal delivery rates, or introduce de-escalation beats to prevent narrative burnout.

---

## 6. Verification & Live Operational Status

* **Active High Port**: `47314` (recorded in [`browser_render/active_port.txt`](file:///Users/akavinash/agy/live-playback-improvised-stream/browser_render/active_port.txt)).
* **Live Web Stage**: [**http://localhost:47314**](http://localhost:47314)
* **Backend API Endpoint**: `POST http://localhost:47314/api/improvise`
* **Real-time Telemetry Stream**: `http://localhost:47314/stream`
