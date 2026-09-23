"""
Jonathan Fox Playback Theatre Story Engine.
Translates user lived-experience offerings into canonical Playback Theatre ritual forms:
1. The Teller's Offering & Conductor Clarification
2. Fluid Sculpture / Pairs (Emotional Polarity Embodiment)
3. The Core Narrative Arc (Platform -> Tilt -> Climax -> Transformation)
4. The Closing Tabloid (Tableau Freeze & Return to Teller)
"""
import re
from typing import Dict, Any, List, Tuple
from dataclasses import dataclass, field

from observability import logged, LOGGER, trace_span

@dataclass
class PlaybackBeat:
    id: int
    phase: str # TELLER_OFFERING, FLUID_SCULPTURE, NARRATIVE_ARC, CLOSING_TABLOID
    speaker: str # CONDUCTOR, A, B, CHORUS
    speaker_name: str
    dialogue: str
    statusA: float
    statusB: float
    tension: float
    targetA: float
    targetB: float
    gestureA: str
    gestureB: str
    camZoom: float
    camLabel: str
    shake: float
    foleyCue: str = "drone_ambient"
    improvised: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "phase": self.phase,
            "speaker": self.speaker,
            "speaker_name": self.speaker_name,
            "dialogue": self.dialogue,
            "statusA": self.statusA,
            "statusB": self.statusB,
            "tension": self.tension,
            "targetA": self.targetA,
            "targetB": self.targetB,
            "gestureA": self.gestureA,
            "gestureB": self.gestureB,
            "camZoom": self.camZoom,
            "camLabel": self.camLabel,
            "shake": self.shake,
            "foleyCue": self.foleyCue,
            "improvised": self.improvised
        }

class EmotionalPolarityAnalyzer:
    """
    Deconstructs user input into opposing psychological forces (Fox & Salas Playback Method).
    """
    POLARITY_MAP = [
        (["betrayal", "knife", "back", "lied", "cheat", "trust", "broken"],
         ("Vulnerable Trust", "Guarded Cynicism", "The cold blade of severed trust.")),
        (["loss", "grief", "death", "goodbye", "farewell", "funeral", "miss", "gone"],
         ("Holding On", "Letting Go", "The ache of empty spaces.")),
        (["fear", "anxiety", "dread", "scared", "terror", "stage", "freeze", "fail"],
         ("The Courage to Step Forward", "The Voice That Says Hide", "Standing at the edge of the abyss.")),
        (["love", "crush", "heart", "confession", "romance", "tender", "date"],
         ("Unguarded Longing", "Self-Protecting Pride", "The fragile whisper across a quiet room.")),
        (["work", "boss", "fired", "office", "burnout", "deadline", "meeting", "career"],
         ("Fierce Ambition", "Suffocating Exhaustion", "The machinery grinding against the soul.")),
        (["anger", "rage", "fury", "fight", "shout", "injustice", "unfair"],
         ("Righteous Indignation", "The Demand for Peace", "A fire that threatens to consume the house.")),
        (["hope", "dream", "new", "beginning", "future", "journey", "escape"],
         ("The Horizon Calling", "The Anchor of the Past", "Taking a step into uncharted light."))
    ]

    @classmethod
    def analyze(cls, text: str) -> Tuple[str, str, str]:
        lower = text.lower()
        for keywords, (side_a, side_b, metaphor) in cls.POLARITY_MAP:
            for kw in keywords:
                if kw in lower:
                    return side_a, side_b, metaphor
        # Default universal human polarity
        return ("The Need to Be Seen", "The Fear of Exposure", "The quiet threshold between hiding and being known.")

class JonathanFoxPlaybackEngine:
    """
    Orchestrates the 4 canonical ritual phases of Jonathan Fox & Jo Salas Playback Theatre.
    """
    @classmethod
    @logged(event="playback_story_generation", service="dramaturgy-engine")
    def generate_full_ritual(cls, teller_prompt: str, starting_beat_id: int = 1) -> List[Dict[str, Any]]:
        clean_prompt = teller_prompt.strip() or "The day everything shifted."
        side_a, side_b, metaphor = EmotionalPolarityAnalyzer.analyze(clean_prompt)

        LOGGER.info(
            event="playback_polarity_crystallized",
            payload={
                "teller_prompt": clean_prompt,
                "side_a": side_a,
                "side_b": side_b,
                "metaphor": metaphor
            }
        )

        beats: List[PlaybackBeat] = []
        b_id = starting_beat_id

        # -------------------------------------------------------------
        # PHASE 1: THE TELLER'S OFFERING & CONDUCTOR CLARIFICATION
        # -------------------------------------------------------------
        beats.append(PlaybackBeat(
            id=b_id,
            phase="TELLER_OFFERING",
            speaker="CONDUCTOR",
            speaker_name="THE CONDUCTOR (FACILITATOR)",
            dialogue=f"Teller, we hear you: '{clean_prompt}'. At the heart of this moment lies {side_a} wrestling with {side_b}. Actors... let's watch.",
            statusA=5.0, statusB=5.0, tension=0.40,
            targetA=0.38, targetB=0.62,
            gestureA="STAND_STILL", gestureB="STAND_STILL",
            camZoom=1.2, camLabel="CONDUCTOR'S INVOCATION", shake=0.0,
            foleyCue="drone_chime"
        ))
        b_id += 1

        # -------------------------------------------------------------
        # PHASE 2: FLUID SCULPTURE & PAIRS (EMOTIONAL POLARITY)
        # -------------------------------------------------------------
        # Actor A embodies Polarity 1 with physical repetition
        beats.append(PlaybackBeat(
            id=b_id,
            phase="FLUID_SCULPTURE",
            speaker="A",
            speaker_name=f"ACTOR A ({side_a.upper()})",
            dialogue=f"I reach out because I cannot stay silent! Every second I hold back, '{clean_prompt}' burns louder!",
            statusA=8.2, statusB=3.5, tension=0.65,
            targetA=0.45, targetB=0.65,
            gestureA="PLEADING_REACH", gestureB="DEFENSIVE_FOLD",
            camZoom=1.45, camLabel=f"FLUID SCULPTURE: {side_a.upper()}", shake=0.3,
            foleyCue="heartbeat_slow"
        ))
        b_id += 1

        # Actor B embodies Polarity 2 with opposing rhythm
        beats.append(PlaybackBeat(
            id=b_id,
            phase="FLUID_SCULPTURE",
            speaker="B",
            speaker_name=f"ACTOR B ({side_b.upper()})",
            dialogue=f"No. Lock the door. If you open yourself to '{clean_prompt}', there is nowhere left to hide.",
            statusA=4.0, statusB=8.5, tension=0.78,
            targetA=0.48, targetB=0.58,
            gestureA="HESITATE_STEP", gestureB="COLD_BARRIER",
            camZoom=1.6, camLabel=f"FLUID PAIR: {side_b.upper()}", shake=0.4,
            foleyCue="drone_swell"
        ))
        b_id += 1

        # -------------------------------------------------------------
        # PHASE 3: THE NARRATIVE ARC (PLATFORM -> TILT -> CLIMAX -> PIVOT)
        # -------------------------------------------------------------
        # 3A. The Platform (The Ordinary World)
        beats.append(PlaybackBeat(
            id=b_id,
            phase="NARRATIVE_ARC",
            speaker="A",
            speaker_name="ACTOR A (TELLER EMBODIMENT)",
            dialogue=f"It started like any other morning. The coffee was lukewarm. But sitting right on the table was '{clean_prompt}'.",
            statusA=6.0, statusB=6.0, tension=0.55,
            targetA=0.42, targetB=0.68,
            gestureA="GESTURE_EXPLAIN", gestureB="LISTENING_ATTENTIVE",
            camZoom=1.4, camLabel="NARRATIVE PLATFORM", shake=0.1,
            foleyCue="clock_tick"
        ))
        b_id += 1

        # 3B. The Tilt (The Disruptive Offer / Conflict Escalation)
        beats.append(PlaybackBeat(
            id=b_id,
            phase="NARRATIVE_ARC",
            speaker="B",
            speaker_name="ACTOR B (THE COUNTER-FORCE)",
            dialogue=f"And you looked me in the eye and acted as if '{clean_prompt}' didn't alter every single promise we made!",
            statusA=4.5, statusB=9.0, tension=0.86,
            targetA=0.46, targetB=0.62,
            gestureA="FLINCH_SURPRISE", gestureB="ACCUSATORY_POINT",
            camZoom=1.8, camLabel="THE THEATRICAL TILT", shake=0.6,
            foleyCue="dramatic_hit"
        ))
        b_id += 1

        # 3C. The Crucible Climax (The Breakthrough Peak)
        beats.append(PlaybackBeat(
            id=b_id,
            phase="NARRATIVE_ARC",
            speaker="A",
            speaker_name="ACTOR A (TELLER EMBODIMENT)",
            dialogue=f"Because I was terrified! Don't you see? '{clean_prompt}' wasn't about winning—it was about surviving the moment!",
            statusA=9.8, statusB=6.2, tension=0.98,
            targetA=0.52, targetB=0.60,
            gestureA="ROAR_VULNERABLE", gestureB="STEP_BACK_AWE",
            camZoom=2.05, camLabel="CLIMACTIC CRUCIBLE", shake=0.85,
            foleyCue="cymbal_swell"
        ))
        b_id += 1

        # 3D. The Transformation / Emotional Realization
        beats.append(PlaybackBeat(
            id=b_id,
            phase="NARRATIVE_ARC",
            speaker="B",
            speaker_name="ACTOR B (THE COUNTER-FORCE)",
            dialogue=f"I hear it now. Underneath all the armor... you just wanted to know you weren't standing alone in the storm.",
            statusA=8.0, statusB=8.0, tension=0.60,
            targetA=0.48, targetB=0.58,
            gestureA="LOWER_GUARD", gestureB="OPEN_PALM_RELEASE",
            camZoom=1.65, camLabel="TRANSFORMATIVE RECOGNITION", shake=0.2,
            foleyCue="drone_harmonic"
        ))
        b_id += 1

        # -------------------------------------------------------------
        # PHASE 4: THE CLOSING TABLOID (TABLEAU & RETURN TO TELLER)
        # -------------------------------------------------------------
        beats.append(PlaybackBeat(
            id=b_id,
            phase="CLOSING_TABLOID",
            speaker="CHORUS",
            speaker_name="THE ENSEMBLE (TABLOID FREEZE)",
            dialogue=f"[TABLOID FREEZE] To our Teller: {metaphor} You survived the crucible, and your story has been honored.",
            statusA=10.0, statusB=10.0, tension=0.30,
            targetA=0.45, targetB=0.55,
            gestureA="FREEZE_TABLOID", gestureB="FREEZE_TABLOID",
            camZoom=1.35, camLabel="CLOSING TABLOID RITUAL", shake=0.0,
            foleyCue="bell_resonance"
        ))

        return [b.to_dict() for b in beats]
