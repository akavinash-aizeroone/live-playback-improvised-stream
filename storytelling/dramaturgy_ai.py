"""
Theatrical & Narrative Dramaturgy AI Engine.
Integrates:
1. Keith Johnstone's Improvisational Theatre (Status Seesaw, Tilts, Re-incorporation)
2. Augusto Boal's Forum Theatre (Spect-Actor Interventions, Anti-Model, Joker arbitration)
3. Jonathan Fox's Playback Theatre (Fluid Sculptures, Emotional Polarities, Tabloids)
4. Robert McKee's Story Architecture (Valence Shifts, Objective vs Obstacle, Turning Points)

Strictly enforces diegetic realism with zero fourth-wall breaks.
"""
import time
import json
from enum import Enum
from typing import Dict, Any, List, Optional

from observability import LOGGER, trace_span
from storytelling.mistral_client import MistralRotatingClient, MISTRAL_CLIENT

class TheatricalTechnique(str, Enum):
    JOHNSTONE_STATUS_TILT = "JOHNSTONE_STATUS_TILT"
    BOAL_FORUM_INTERVENTION = "BOAL_FORUM_INTERVENTION"
    FOX_PLAYBACK_RITUAL = "FOX_PLAYBACK_RITUAL"
    MCKEE_VALUE_SHIFT = "MCKEE_VALUE_SHIFT"

SCENE_CONTEXTS = {
    "pulp_fiction": {
        "title": "Pulp Fiction - The Brett Interrogation",
        "charA": "Jules Winnfield (Hitman enforcing Marcellus Wallace's will, righteous wrath)",
        "charB": "Brett (Terrified college kid caught stealing Marcellus Wallace's property)",
        "initial_statusA": 9.5,
        "initial_statusB": 2.0,
        "oppressor": "charA",
        "oppressed": "charB",
        "given_circumstances": "Apartment room in North Hollywood. A black briefcase sits on the counter. Brett is backed against the wall."
    },
    "a_few_good_men": {
        "title": "A Few Good Men - The Code Red Climax",
        "charA": "Lt. Daniel Kaffee (Navy JAG defense attorney pursuing systemic truth)",
        "charB": "Col. Nathan Jessep (Hardened Marine Commander who ordered the Code Red at Guantanamo Bay)",
        "initial_statusA": 8.0,
        "initial_statusB": 9.8,
        "oppressor": "charB",
        "oppressed": "charA",
        "given_circumstances": "Military courtroom, high heat. Jessep is in the witness stand; Kaffee has cornered him on the flight log contradictions."
    },
    "dark_knight": {
        "title": "The Dark Knight - The Hospital Anarchy Dialectic",
        "charA": "The Joker (Agent of chaos holding a detonator, unmasking social hypocrisy)",
        "charB": "Harvey Dent (Burned Gotham DA on a hospital bed, succumbing to vengeance)",
        "initial_statusA": 9.2,
        "initial_statusB": 4.5,
        "oppressor": "charA",
        "oppressed": "charB",
        "given_circumstances": "Gotham General Hospital room. Dent's face is half-burned. The Joker hands Dent a revolver and places it to his own head."
    },
    "whiplash": {
        "title": "Whiplash - The Tempo Execution",
        "charA": "Terence Fletcher (Ruthless jazz conservatory conductor demanding perfection)",
        "charB": "Andrew Neiman (Obsessive young jazz drummer willing to bleed for greatness)",
        "initial_statusA": 10.0,
        "initial_statusB": 3.0,
        "oppressor": "charA",
        "oppressed": "charB",
        "given_circumstances": "Rehearsal Studio B at Shaffer Conservatory. The band sits in silence. Fletcher is inches from Neiman's face."
    },
    "social_network": {
        "title": "The Social Network - The 0.03% Confrontation",
        "charA": "Eduardo Saverin (Betrayed co-founder whose equity was secretly diluted)",
        "charB": "Mark Zuckerberg (Quiet, cold architect of Facebook focused purely on code and dominance)",
        "initial_statusA": 9.0,
        "initial_statusB": 6.5,
        "oppressor": "charB",
        "oppressed": "charA",
        "given_circumstances": "Palo Alto Facebook office. Eduardo storms into the glass boardroom holding the restructured shareholding agreement."
    }
}

VALID_GESTURES = [
    "POINT", "DRAW_PISTOL", "ROAR_AIM", "ROAR_EZEKIEL_CLIMAX",
    "PLEADING_TERROR", "FLINCH_TERROR", "STAND_FIRM", "ROAR",
    "GLARE", "LEAN_INTO_FACE", "TREMBLING_HANDS", "RAISE_FIST_HALT",
    "TENSE_DRUMSTICKS", "SLAM_TABLE", "MONOTONE_GLARE", "ARMS_OUT_SAVIOR",
    "SUBMISSIVE_BOW", "OFFER_OBJECT"
]

class DramaturgyAIEngine:
    """
    Applied AI Theatrical Dramaturgy Engine.
    Leverages rotating Mistral AI models to synthesize authentic, in-character,
    theatrically structured dramatic beats with zero fourth-wall breaks.
    """
    def __init__(self, client: Optional[MistralRotatingClient] = None):
        self.client = client or MISTRAL_CLIENT

    def _build_system_prompt(self, technique: TheatricalTechnique, scene_info: Dict[str, Any]) -> str:
        base_prompt = f"""You are the Master Theatrical Dramaturg and Autonomous Scriptwriter for an interactive live theatrical puppetry stream.
The active scene is: {scene_info['title']}
Character A: {scene_info['charA']}
Character B: {scene_info['charB']}
Given Circumstances: {scene_info['given_circumstances']}

ABSOLUTE CARDINAL RULE - ZERO FOURTH-WALL BREAKS:
- Characters MUST NEVER acknowledge that they are in an AI simulation, a live stream, or an improv game.
- Characters MUST NEVER say: 'Did you just say X?', 'Why did you type X?', 'Hold on a second, who brought up X?'.
- Any word, object, or concept provided by the spectator must be IMMEDIATELY and DIEGETICALLY internalized as an organic, in-universe reality with high emotional stakes.
  Example in Pulp Fiction if given 'violin': Jules demands to know if Brett hid Marcellus's antique Stradivarius; Brett screams that it was delivered to the pawnshop.
  Example in A Few Good Men if given 'radar': Kaffee asks if the radar sweep was falsified; Jessep roars about perimeter radar shielding troops.
"""
        if technique == TheatricalTechnique.JOHNSTONE_STATUS_TILT:
            base_prompt += """
THEATRICAL FRAMEWORK: KEITH JOHNSTONE IMPROVISATION & STATUS SEESAW:
- Track relative status (1.0 to 10.0). Status is a seesaw: when one character raises status, the other must yield or resist.
- Introduce an immediate TILT: a dramatic disruption of the scene's balance caused by the injected element.
- Maintain re-incorporation: tie the offer into previous scene secrets or obligations.
"""
        elif technique == TheatricalTechnique.BOAL_FORUM_INTERVENTION:
            base_prompt += f"""
THEATRICAL FRAMEWORK: AUGUSTO BOAL'S FORUM THEATRE (THEATRE OF THE OPPRESSED):
- Oppressor: {scene_info['oppressor']} | Oppressed: {scene_info['oppressed']}
- The spectator's word is a TACTICAL COUNTER-OFFENSIVE used by the oppressed character against the oppressor's systemic leverage.
- The oppressor resists strongly; only conceding ground if the tactic attacks their core vulnerability.
"""
        elif technique == TheatricalTechnique.FOX_PLAYBACK_RITUAL:
            base_prompt += """
THEATRICAL FRAMEWORK: JONATHAN FOX'S PLAYBACK THEATRE RITUAL FORMS:
- The input is an emotional offering from the audience.
- Embody the internal polarity (e.g. Fear vs Duty, Guilt vs Freedom).
- Structure the beats to escalate to a poignant climax, culminating in a frozen tableau (tabloid) gesture.
"""
        elif technique == TheatricalTechnique.MCKEE_VALUE_SHIFT:
            base_prompt += """
THEATRICAL FRAMEWORK: ROBERT MCKEE'S STORY ARCHITECTURE:
- Every beat must contain a clear VALUE CHARGE TRANSITION (Positive to Negative or Negative to Positive).
- Character objectives must collide directly with the obstacle.
- The turning point must create a gap between expectation and result.
"""

        base_prompt += f"""
OUTPUT FORMAT:
You MUST respond with a single valid JSON object with EXACTLY this structure:
{{
  "technique": "{technique.value}",
  "value_shift": "+ to -" or "- to +",
  "dramaturgical_analysis": "One concise sentence explaining the status and narrative shift.",
  "beats": [
    {{
      "id": 1,
      "speaker": "A",
      "dialogue": "In-character dialogue line",
      "statusA": 9.4,
      "statusB": 2.1,
      "tension": 0.88,
      "targetA": 0.52,
      "targetB": 0.70,
      "gestureA": "DRAW_PISTOL",
      "gestureB": "FLINCH_TERROR",
      "camZoom": 1.7,
      "camLabel": "THE TILT",
      "shake": 0.5,
      "theatrical_note": "A asserts dominance via prop"
    }},
    {{
      "id": 2,
      "speaker": "B",
      "dialogue": "In-character reaction line",
      "statusA": 9.2,
      "statusB": 3.5,
      "tension": 0.94,
      "targetA": 0.54,
      "targetB": 0.70,
      "gestureA": "ROAR_AIM",
      "gestureB": "PLEADING_TERROR",
      "camZoom": 1.9,
      "camLabel": "COUNTER ESCALATION",
      "shake": 0.7,
      "theatrical_note": "B struggles against oppression"
    }},
    {{
      "id": 3,
      "speaker": "A",
      "dialogue": "Climactic resolution line",
      "statusA": 10.0,
      "statusB": 1.0,
      "tension": 1.0,
      "targetA": 0.58,
      "targetB": 0.70,
      "gestureA": "ROAR_EZEKIEL_CLIMAX",
      "gestureB": "FLINCH_TERROR",
      "camZoom": 2.1,
      "camLabel": "CLIMACTIC PEAK",
      "shake": 1.0,
      "theatrical_note": "A reaches peak power"
    }}
  ]
}}

Available gestures: {', '.join(VALID_GESTURES)}.
Ensure 2 to 3 beats total.
"""
        return base_prompt

    def generate(
        self,
        scene_key: str,
        user_word: str,
        technique: TheatricalTechnique = TheatricalTechnique.JOHNSTONE_STATUS_TILT,
        current_beat_id: int = 1
    ) -> Dict[str, Any]:
        """
        Synthesizes live theatrical beats using rotating Mistral AI keys with fallback safety.
        """
        clean_word = user_word.strip() or "the ledger"
        scene_info = SCENE_CONTEXTS.get(scene_key, SCENE_CONTEXTS["pulp_fiction"])

        system_prompt = self._build_system_prompt(technique, scene_info)
        user_prompt = f"""Spectator Injected Offer / Word: "{clean_word}"
Starting Beat ID: {current_beat_id + 1}
Generate the next 2-3 beats incorporating this offer organically into the scene's stakes."""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        with trace_span("dramaturgy_ai_generate", service="dramaturgy-engine", attributes={"scene": scene_key, "technique": technique.value, "word": clean_word}):
            llm_result = self.client.complete(messages, temperature=0.75, json_mode=True)

            if llm_result.get("success") and isinstance(llm_result.get("content"), dict):
                data = llm_result["content"]
                raw_beats = data.get("beats", [])
                formatted_beats = []

                for idx, b in enumerate(raw_beats):
                    bid = current_beat_id + idx + 1
                    speaker = b.get("speaker", "A" if idx % 2 == 0 else "B")
                    formatted_beats.append({
                        "id": bid,
                        "speaker": speaker,
                        "dialogue": b.get("dialogue", "..."),
                        "statusA": float(b.get("statusA", 8.0)),
                        "statusB": float(b.get("statusB", 3.0)),
                        "tension": float(b.get("tension", 0.85)),
                        "targetA": float(b.get("targetA", 0.52)),
                        "targetB": float(b.get("targetB", 0.70)),
                        "gestureA": b.get("gestureA", "POINT"),
                        "gestureB": b.get("gestureB", "FLINCH_TERROR"),
                        "camZoom": float(b.get("camZoom", 1.7)),
                        "camLabel": b.get("camLabel", f"AI {technique.name}"),
                        "shake": float(b.get("shake", 0.5)),
                        "improvised": True
                    })

                LOGGER.info(
                    "dramaturgy.beats_synthesized",
                    service="dramaturgy-engine",
                    payload={
                        "scene": scene_key,
                        "technique": technique.value,
                        "beats_count": len(formatted_beats),
                        "key_used": llm_result.get("key_used"),
                        "duration_ms": llm_result.get("duration_ms")
                    }
                )

                return {
                    "success": True,
                    "technique": technique.value,
                    "value_shift": data.get("value_shift", "+ to -"),
                    "dramaturgical_analysis": data.get("dramaturgical_analysis", "Dynamic status tilt via spectator offer."),
                    "key_used": llm_result.get("key_used"),
                    "duration_ms": llm_result.get("duration_ms"),
                    "improvised_beats": formatted_beats
                }

        # High-Fidelity Theatrical Algorithmic Fallback if Mistral is offline
        return self._generate_algorithmic_fallback(scene_key, clean_word, technique, current_beat_id)

    def _generate_algorithmic_fallback(
        self,
        scene_key: str,
        clean_word: str,
        technique: TheatricalTechnique,
        current_beat_id: int
    ) -> Dict[str, Any]:
        """Ensures the live show never halts even during upstream cloud outages."""
        LOGGER.warn("dramaturgy.using_algorithmic_fallback", service="dramaturgy-engine", payload={"scene": scene_key, "word": clean_word})

        if scene_key == "pulp_fiction":
            beats = [
                {
                    "id": current_beat_id + 1,
                    "speaker": "A",
                    "dialogue": f"You think Marcellus Wallace didn't know about '{clean_word}'?! Brett, look at me! You think my boss sent his most loyal shepherd across town just to let '{clean_word}' slip out of this room?!",
                    "statusA": 9.6, "statusB": 2.0, "tension": 0.88,
                    "targetA": 0.52, "targetB": 0.70, "gestureA": "DRAW_PISTOL", "gestureB": "FLINCH_TERROR",
                    "camZoom": 1.7, "camLabel": f"JOHNSTONE TILT: {clean_word[:12].upper()}", "shake": 0.5, "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": f"Jules, I swear on everything holy! '{clean_word.capitalize()}' was never meant to cross Marcellus! We were protecting it in the cupboard until you arrived!",
                    "statusA": 9.2, "statusB": 3.8, "tension": 0.94,
                    "targetA": 0.54, "targetB": 0.70, "gestureA": "ROAR_AIM", "gestureB": "PLEADING_TERROR",
                    "camZoom": 1.9, "camLabel": "DESPERATE DEFENSE", "shake": 0.7, "improvised": True
                },
                {
                    "id": current_beat_id + 3,
                    "speaker": "A",
                    "dialogue": f"Then why is '{clean_word}' smelling like treason to me, Brett?! Because the righteous man does not barter over '{clean_word}'!",
                    "statusA": 10.0, "statusB": 1.0, "tension": 1.0,
                    "targetA": 0.58, "targetB": 0.70, "gestureA": "ROAR_EZEKIEL_CLIMAX", "gestureB": "FLINCH_TERROR",
                    "camZoom": 2.1, "camLabel": "THE WRATH OF JULES", "shake": 1.1, "improvised": True
                }
            ]
        elif scene_key == "a_few_good_men":
            beats = [
                {
                    "id": current_beat_id + 1,
                    "speaker": "A",
                    "dialogue": f"Colonel Jessep, isn't it true that '{clean_word}' was the exact pretext used to authorize the transfer order?",
                    "statusA": 8.8, "statusB": 9.2, "tension": 0.85,
                    "targetA": 0.50, "targetB": 0.72, "gestureA": "POINT", "gestureB": "GLARE",
                    "camZoom": 1.5, "camLabel": f"BOAL FORUM INTERVENTION: {clean_word[:12].upper()}", "shake": 0.4, "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": f"You sit there in your crisp whites and lecture me about '{clean_word}'?! '{clean_word.capitalize()}' saved American lives at Windward Point!",
                    "statusA": 8.5, "statusB": 10.0, "tension": 0.96,
                    "targetA": 0.50, "targetB": 0.70, "gestureA": "STAND_FIRM", "gestureB": "ROAR",
                    "camZoom": 1.85, "camLabel": "JESSEP COUNTER-OFFENSIVE", "shake": 0.9, "improvised": True
                }
            ]
        else:
            beats = [
                {
                    "id": current_beat_id + 1,
                    "speaker": "A",
                    "dialogue": f"You brought '{clean_word}' into this room because you knew it would tear open our foundation!",
                    "statusA": 9.0, "statusB": 3.0, "tension": 0.88,
                    "targetA": 0.52, "targetB": 0.70, "gestureA": "POINT", "gestureB": "FLINCH_TERROR",
                    "camZoom": 1.7, "camLabel": "THEATRICAL TILT", "shake": 0.5, "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": f"'{clean_word.capitalize()}' wasn't a weapon until you turned it into one!",
                    "statusA": 8.5, "statusB": 4.5, "tension": 0.95,
                    "targetA": 0.54, "targetB": 0.70, "gestureA": "STAND_FIRM", "gestureB": "PLEADING_TERROR",
                    "camZoom": 1.9, "camLabel": "DEFENSE RESPONSE", "shake": 0.7, "improvised": True
                }
            ]

        return {
            "success": True,
            "fallback": True,
            "technique": technique.value,
            "value_shift": "+ to -",
            "dramaturgical_analysis": "Deterministic dramaturgical fallback executed (cloud offline).",
            "key_used": "deterministic-dramaturgy-ruleset",
            "duration_ms": 0.1,
            "improvised_beats": beats
        }

# Global Singleton
THEATRICAL_ENGINE = DramaturgyAIEngine()
