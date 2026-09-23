"""
Theatrical & Narrative Dramaturgy AI Engine.
Advanced Applied AI Storytelling Architecture integrating:
1. Hemingway's Iceberg Theory & Stanislavski Subtext (Prompt Transmutation without mechanical parroting)
2. Keith Johnstone's Improvisational Theatre (Status Seesaw, Dramatic Tilts, Re-incorporation)
3. Augusto Boal's Forum Theatre (Spect-Actor Tactical Interventions vs Systemic Oppression)
4. Jonathan Fox's Playback Theatre (Emotional Polarity Pairs & Closing Tabloid Tableaux)
5. Robert McKee's Story Architecture (Valence Shifts, Objective vs Obstacle, Turning Points)
6. Chekhov's Gun (Dramatic Planting and Inevitable Climactic Discharge)

Enforces deep diegetic realism, character objectives, and zero fourth-wall breaks.
"""
import time
import json
from enum import Enum
from typing import Dict, Any, List, Optional

from observability import LOGGER, trace_span
from storytelling.mistral_client import MistralRotatingClient, MISTRAL_CLIENT

class TheatricalTechnique(str, Enum):
    SUBTEXT_CATALYST = "SUBTEXT_CATALYST"
    JOHNSTONE_STATUS_TILT = "JOHNSTONE_STATUS_TILT"
    BOAL_FORUM_INTERVENTION = "BOAL_FORUM_INTERVENTION"
    FOX_PLAYBACK_RITUAL = "FOX_PLAYBACK_RITUAL"
    MCKEE_VALUE_SHIFT = "MCKEE_VALUE_SHIFT"
    CHEKHOV_GUN_PAYOFF = "CHEKHOV_GUN_PAYOFF"

SCENE_CONTEXTS = {
    "pulp_fiction": {
        "title": "Pulp Fiction - The Brett Interrogation",
        "charA": "Jules Winnfield (Hitman enforcing Marcellus Wallace's will, righteous wrath)",
        "charB": "Brett (Terrified college kid caught stealing Marcellus Wallace's property)",
        "initial_statusA": 9.5,
        "initial_statusB": 2.0,
        "oppressor": "charA",
        "oppressed": "charB",
        "world_subtext": "Los Angeles underworld crime, divine judgment, sacred contracts, stolen briefcases.",
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
        "world_subtext": "Military honor codes, chain of command, perjury, perimeter defense, sacrifice vs complicity.",
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
        "world_subtext": "Gotham corruption, moral collapse, arbitrary chance, fairness vs nihilism.",
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
        "world_subtext": "Obsession, psychological abuse, greatness vs mediocrity, bleeding fingers, tempo.",
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
        "world_subtext": "Silicon Valley ambition, legal betrayal, loyalty vs valuation, friendship as collateral damage.",
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
    Applied AI Master Theatrical Dramaturgy Engine.
    Converts spectator offers into deep narrative subtext and multi-technique dramatic beats
    WITHOUT mechanically repeating or quoting the user's literal words.
    """
    def __init__(self, client: Optional[MistralRotatingClient] = None):
        self.client = client or MISTRAL_CLIENT

    def _build_system_prompt(self, technique: TheatricalTechnique, scene_info: Dict[str, Any]) -> str:
        base_prompt = f"""You are the Master Theatrical Dramaturg and Screenwriter for an interactive live theatrical puppetry stream.
The active scene is: {scene_info['title']}
Character A: {scene_info['charA']}
Character B: {scene_info['charB']}
World Subtext: {scene_info['world_subtext']}
Given Circumstances: {scene_info['given_circumstances']}

===========================================================================
THE GOLDEN RULE OF APPLIED AI DRAMATURGY:
DO NOT MECHANICALLY PARROT OR QUOTE THE SPECTATOR'S LITERAL WORDS!
===========================================================================
- The spectator's input is NOT a dialogue quote to be recited. It is the INCITING CATALYST, HIDDEN SUBTEXT, or UNDERLYING CRISIS.
- The characters MUST NOT say: 'Did you just say X?', 'You brought up X', or awkwardly insert 'X' in quotation marks.
- Instead, TRANSMUTE the spectator's offer into the character's organic psychology, secrets, evidence, or physical actions:
  * Example in Pulp Fiction if given 'poisoned coffee': Jules doesn't say the words 'poisoned coffee'. Jules demands to know why Brett brewed a fresh pot at 7:00 AM before anyone arrived, accuses him of trying to drug Marcellus's couriers, and demands he drink from the steaming mug himself.
  * Example in A Few Good Men if given 'broken promises': Kaffee doesn't say 'you broke your promise'. Kaffee corners Jessep on the private off-the-record call with Markinson fifteen minutes after Santiago died.
  * Example in The Dark Knight if given 'stolen diamond': The Joker doesn't talk about a literal diamond. He mocks Dent for worshipping cold carbon locked in a mob vault while Gotham's bridges are already rigged with gasoline.
  * Example in Whiplash if given 'bleeding hands': Fletcher doesn't say 'your hands are bleeding'. Fletcher inspects the bloodstains on the snare skin and whispers that physical agony is merely the admission price to genius.

ACTIVE THEATRICAL TECHNIQUE: {technique.value}
"""
        if technique == TheatricalTechnique.SUBTEXT_CATALYST:
            base_prompt += """
TECHNIQUE FOCUS: HEMINGWAY'S ICEBERG THEORY & STANISLAVSKI SUBTEXT:
- The spoken dialogue is merely the 10% visible above water.
- The spectator's offer forms the massive 90% submerged beneath the surface.
- Characters argue with fierce urgency about surface details that represent the deep existential conflict.
"""
        elif technique == TheatricalTechnique.JOHNSTONE_STATUS_TILT:
            base_prompt += """
TECHNIQUE FOCUS: KEITH JOHNSTONE IMPROVISATION & STATUS SEESAW:
- Track relative status (1.0 to 10.0). Status is a continuous seesaw.
- The spectator's offer causes a dramatic TILT—an irreversible disruption of the existing power balance.
- Execute subtle status shifts (raising self, lowering other, or sudden voluntary submission).
"""
        elif technique == TheatricalTechnique.BOAL_FORUM_INTERVENTION:
            base_prompt += f"""
TECHNIQUE FOCUS: AUGUSTO BOAL'S FORUM THEATRE (THEATRE OF THE OPPRESSED):
- Oppressor: {scene_info['oppressor']} | Oppressed: {scene_info['oppressed']}
- The spectator's offer represents a tactical intervention attempting to expose or overturn systemic oppression.
- The oppressor resists fiercely; only conceding if cornered by an undeniable contradiction.
"""
        elif technique == TheatricalTechnique.FOX_PLAYBACK_RITUAL:
            base_prompt += """
TECHNIQUE FOCUS: JONATHAN FOX'S PLAYBACK THEATRE RITUAL FORMS:
- Embody the emotional polarity (e.g. Vulnerable Longing vs Hardened Defiance).
- Escalate the emotional stakes to a piercing climax, ending in a symbolic physical tableau freeze.
"""
        elif technique == TheatricalTechnique.MCKEE_VALUE_SHIFT:
            base_prompt += """
TECHNIQUE FOCUS: ROBERT MCKEE'S STORY ARCHITECTURE:
- Every beat MUST execute a clear VALUE CHARGE TRANSITION (+ to - or - to +).
- Character objectives collide head-on with an unyielding obstacle, opening a gap between expectation and reality.
"""
        elif technique == TheatricalTechnique.CHEKHOV_GUN_PAYOFF:
            base_prompt += """
TECHNIQUE FOCUS: CHEKHOV'S GUN & PLANT/PAYOFF:
- Plant the consequence of the spectator's offer in the first beat as an unspoken threat.
- Detonate that threat in the final beat with devastating dramatic finality.
"""

        base_prompt += f"""
OUTPUT FORMAT SPECIFICATION:
You MUST respond with a single valid JSON object with EXACTLY this structure:
{{
  "technique": "{technique.value}",
  "transmuted_subtext": "One concise phrase describing the underlying secret/conflict derived from the offer (without literal quoting).",
  "value_shift": "+ to -" or "- to +",
  "dramaturgical_analysis": "One sentence explaining the psychological collision and status moves.",
  "beats": [
    {{
      "id": 1,
      "speaker": "A",
      "dialogue": "Authentic, cinematic dialogue line capturing the subtext organically.",
      "statusA": 9.4,
      "statusB": 2.1,
      "tension": 0.88,
      "targetA": 0.52,
      "targetB": 0.70,
      "gestureA": "DRAW_PISTOL",
      "gestureB": "FLINCH_TERROR",
      "camZoom": 1.7,
      "camLabel": "SUBTEXT UNMASKED",
      "shake": 0.5,
      "theatrical_note": "A applies status pressure"
    }},
    {{
      "id": 2,
      "speaker": "B",
      "dialogue": "Authentic in-character reaction escalating the conflict.",
      "statusA": 9.2,
      "statusB": 3.5,
      "tension": 0.94,
      "targetA": 0.54,
      "targetB": 0.70,
      "gestureA": "ROAR_AIM",
      "gestureB": "PLEADING_TERROR",
      "camZoom": 1.9,
      "camLabel": "DESPERATE DEFENSE",
      "shake": 0.7,
      "theatrical_note": "B struggles under cross-examination"
    }},
    {{
      "id": 3,
      "speaker": "A",
      "dialogue": "Climactic resolution line sealing the dramatic turning point.",
      "statusA": 10.0,
      "statusB": 1.0,
      "tension": 1.0,
      "targetA": 0.58,
      "targetB": 0.70,
      "gestureA": "ROAR_EZEKIEL_CLIMAX",
      "gestureB": "FLINCH_TERROR",
      "camZoom": 2.2,
      "camLabel": "TURNING POINT CLIMAX",
      "shake": 1.0,
      "theatrical_note": "Peak dramatic confrontation"
    }}
  ]
}}

Available gestures: {', '.join(VALID_GESTURES)}.
Ensure 2 to 3 beats total. Zero fourth-wall breaks. Zero literal quotation of the user's input.
"""
        return base_prompt

    def generate(
        self,
        scene_key: str,
        user_word: str,
        technique: Optional[TheatricalTechnique] = None,
        current_beat_id: int = 1
    ) -> Dict[str, Any]:
        """
        Synthesizes live theatrical beats using rotating Mistral AI keys with fallback safety.
        Transmutes the spectator offer into rich narrative subtext without mechanical parroting.
        """
        clean_word = user_word.strip() or "the hidden ledger"
        tech = technique or TheatricalTechnique.SUBTEXT_CATALYST
        scene_info = SCENE_CONTEXTS.get(scene_key, SCENE_CONTEXTS["pulp_fiction"])

        system_prompt = self._build_system_prompt(tech, scene_info)
        user_prompt = f"""Spectator Injected Offer / Catalyst: "{clean_word}"
Starting Beat ID: {current_beat_id + 1}
Instructions: Transmute this offer into the scene's unspoken subtext, hidden evidence, or stakes. DO NOT mechanically quote '{clean_word}' verbatim in dialogue quotes; weave its dramatic consequences directly into the characters' objectives, status moves, and blocking."""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        with trace_span("dramaturgy_ai_generate", service="dramaturgy-engine", attributes={"scene": scene_key, "technique": tech.value, "catalyst": clean_word}):
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
                        "camLabel": b.get("camLabel", f"AI {tech.name}"),
                        "shake": float(b.get("shake", 0.5)),
                        "improvised": True
                    })

                LOGGER.info(
                    "dramaturgy.beats_synthesized",
                    service="dramaturgy-engine",
                    payload={
                        "scene": scene_key,
                        "technique": tech.value,
                        "beats_count": len(formatted_beats),
                        "transmuted_subtext": data.get("transmuted_subtext", clean_word),
                        "key_used": llm_result.get("key_used"),
                        "duration_ms": llm_result.get("duration_ms")
                    }
                )

                return {
                    "success": True,
                    "technique": tech.value,
                    "transmuted_subtext": data.get("transmuted_subtext", f"Underlying catalyst: {clean_word}"),
                    "value_shift": data.get("value_shift", "+ to -"),
                    "dramaturgical_analysis": data.get("dramaturgical_analysis", "Subtextual transmutation executed without literal parroting."),
                    "key_used": llm_result.get("key_used"),
                    "duration_ms": llm_result.get("duration_ms"),
                    "improvised_beats": formatted_beats
                }

        # High-Fidelity Theatrical Algorithmic Fallback (Subtext-driven, zero literal quotes)
        return self._generate_algorithmic_fallback(scene_key, clean_word, tech, current_beat_id)

    def _generate_algorithmic_fallback(
        self,
        scene_key: str,
        clean_word: str,
        technique: TheatricalTechnique,
        current_beat_id: int
    ) -> Dict[str, Any]:
        """Subtextual, non-literal fallback guaranteeing the live stream never halts."""
        LOGGER.warn("dramaturgy.using_algorithmic_fallback", service="dramaturgy-engine", payload={"scene": scene_key, "catalyst": clean_word})

        if scene_key == "pulp_fiction":
            beats = [
                {
                    "id": current_beat_id + 1,
                    "speaker": "A",
                    "dialogue": "You think Marcellus Wallace didn't smell the treachery the second you packed your bags, Brett?! Look at me! You think my boss sent his most loyal shepherd across town just to let this betrayal slide?!",
                    "statusA": 9.6, "statusB": 2.0, "tension": 0.88,
                    "targetA": 0.52, "targetB": 0.70, "gestureA": "DRAW_PISTOL", "gestureB": "FLINCH_TERROR",
                    "camZoom": 1.7, "camLabel": "SUBTEXT UNMASKED", "shake": 0.5, "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": "Jules, I swear on everything holy! It was never meant to cross Marcellus! We were holding it under lock and key until you arrived!",
                    "statusA": 9.2, "statusB": 3.8, "tension": 0.94,
                    "targetA": 0.54, "targetB": 0.70, "gestureA": "ROAR_AIM", "gestureB": "PLEADING_TERROR",
                    "camZoom": 1.9, "camLabel": "DESPERATE DEFENSE", "shake": 0.7, "improvised": True
                },
                {
                    "id": current_beat_id + 3,
                    "speaker": "A",
                    "dialogue": "Then why does this whole room reek of a double-cross, Brett?! Because the righteous man does not barter with thieves!",
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
                    "dialogue": "Colonel Jessep, isn't it true that the 0200 perimeter watch logs were doctored to conceal the exact route used for the transfer order?",
                    "statusA": 8.8, "statusB": 9.2, "tension": 0.85,
                    "targetA": 0.50, "targetB": 0.72, "gestureA": "POINT", "gestureB": "GLARE",
                    "camZoom": 1.5, "camLabel": "FORUM INTERVENTION", "shake": 0.4, "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": "You sit there in your crisp whites with your Harvard pedigree and question how I preserve blood at the fence line?! My orders saved lives at Windward Point!",
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
                    "dialogue": "You opened this door knowing it would tear apart the foundation we spent years building.",
                    "statusA": 9.0, "statusB": 3.0, "tension": 0.88,
                    "targetA": 0.52, "targetB": 0.70, "gestureA": "POINT", "gestureB": "FLINCH_TERROR",
                    "camZoom": 1.7, "camLabel": "THEATRICAL TILT", "shake": 0.5, "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": "The foundation was already rotted! I just had the courage to shine a lantern into the cellar!",
                    "statusA": 8.5, "statusB": 4.5, "tension": 0.95,
                    "targetA": 0.54, "targetB": 0.70, "gestureA": "STAND_FIRM", "gestureB": "PLEADING_TERROR",
                    "camZoom": 1.9, "camLabel": "DEFENSE RESPONSE", "shake": 0.7, "improvised": True
                }
            ]

        return {
            "success": True,
            "fallback": True,
            "technique": technique.value,
            "transmuted_subtext": f"Subtextual transmutation: {clean_word}",
            "value_shift": "+ to -",
            "dramaturgical_analysis": "Subtextual algorithmic fallback executed (cloud offline).",
            "key_used": "deterministic-dramaturgy-ruleset",
            "duration_ms": 0.1,
            "improvised_beats": beats
        }

# Global Singleton
THEATRICAL_ENGINE = DramaturgyAIEngine()
