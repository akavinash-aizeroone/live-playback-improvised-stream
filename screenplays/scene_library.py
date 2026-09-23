"""
Screenplay Library: Iconic Cinematic & Theatrical Showdowns
Includes exact dialogue, status coordinates, kinematic stage targets,
and Augusto Boal intervention checkpoints.
"""

SCENE_A_FEW_GOOD_MEN = {
    "title": "A Few Good Men (1992)",
    "playwright": "Aaron Sorkin",
    "location": "Guantanamo Bay Court-Martial Courtroom",
    "prop_type": "COURTROOM",
    "characters": {
        "AGENT_A": {
            "name": "LT. DANIEL KAFFEE",
            "role": "Lead Defense Counsel (Prosecuting the Colonel)",
            "color": "#38bdf8",
            "voice_pitch": 1.15,
            "voice_rate": 1.05
        },
        "AGENT_B": {
            "name": "COL. NATHAN R. JESSEP",
            "role": "Commander, Marine Barracks Guantanamo",
            "color": "#f87171",
            "voice_pitch": 0.82,
            "voice_rate": 0.95
        }
    },
    "props": [
        {"name": "Witness Stand", "type": "RAIL", "x": 0.75, "y": 0.72},
        {"name": "Defense Counsel Table", "type": "TABLE", "x": 0.22, "y": 0.72}
    ],
    "beats": [
        {
            "id": 1,
            "speaker": "AGENT_A",
            "dialogue": "Colonel Jessep, did you order the Code Red?",
            "status_a": 7.0,
            "status_b": 9.5,
            "tension": 0.55,
            "target_x_a": 0.32,
            "target_x_b": 0.78,
            "gesture": "POINT_LEGAL_PAD",
            "cam_zoom": 1.0,
            "cam_label": "ESTABLISHING TWO-SHOT"
        },
        {
            "id": 2,
            "speaker": "AGENT_B",
            "dialogue": "You don't have to answer that question!",
            "status_a": 7.0,
            "status_b": 9.8,
            "tension": 0.62,
            "target_x_a": 0.32,
            "target_x_b": 0.78,
            "gesture": "CHEST_PUFF",
            "cam_zoom": 1.1,
            "cam_label": "MEDIUM ON JESSEP",
            "shake": 0.3
        },
        {
            "id": 3,
            "speaker": "AGENT_A",
            "dialogue": "Your Honor, I have the right to question the witness on this issue!",
            "status_a": 7.8,
            "status_b": 9.5,
            "tension": 0.70,
            "target_x_a": 0.44,
            "target_x_b": 0.78,
            "gesture": "STRIDE_FORWARD",
            "cam_zoom": 1.2,
            "cam_label": "PUSH-IN ON COUNSEL"
        },
        {
            "id": 4,
            "speaker": "AGENT_B",
            "dialogue": "I'll answer the question. You want answers?",
            "status_a": 8.0,
            "status_b": 9.5,
            "tension": 0.75,
            "target_x_a": 0.48,
            "target_x_b": 0.74,
            "gesture": "LEAN_OVER_RAIL",
            "cam_zoom": 1.3,
            "cam_label": "TIGHT PROFILE TWO-SHOT"
        },
        {
            "id": 5,
            "speaker": "AGENT_A",
            "dialogue": "I think I'm entitled to them.",
            "status_a": 8.5,
            "status_b": 9.2,
            "tension": 0.80,
            "target_x_a": 0.52,
            "target_x_b": 0.72,
            "gesture": "STEADY_STANCE",
            "cam_zoom": 1.35,
            "cam_label": "CONFRONTATION PROXEMIC"
        },
        {
            "id": 6,
            "speaker": "AGENT_B",
            "dialogue": "You want answers?!",
            "status_a": 8.5,
            "status_b": 9.8,
            "tension": 0.88,
            "target_x_a": 0.52,
            "target_x_b": 0.70,
            "gesture": "STEP_OUT_OF_STAND",
            "cam_zoom": 1.45,
            "cam_label": "STEP-DOWN TENSION"
        },
        {
            "id": 7,
            "speaker": "AGENT_A",
            "dialogue": "I WANT THE TRUTH!",
            "status_a": 9.6,
            "status_b": 9.8,
            "tension": 0.96,
            "target_x_a": 0.56,
            "target_x_b": 0.70,
            "gesture": "BOTH_ARMS_FORWARD",
            "cam_zoom": 1.6,
            "cam_label": "CHOKE-POINT CLOSEUP",
            "shake": 0.5
        },
        {
            "id": 8,
            "speaker": "AGENT_B",
            "dialogue": "YOU CAN'T HANDLE THE TRUTH!",
            "status_a": 8.2,
            "status_b": 10.0,
            "tension": 1.0,
            "target_x_a": 0.54,
            "target_x_b": 0.68,
            "gesture": "ROAR_EXPAND_SCALE",
            "cam_zoom": 1.8,
            "cam_label": "CLIMAX EXTREME CLOSEUP",
            "shake": 0.9
        },
        {
            "id": 9,
            "speaker": "AGENT_B",
            "dialogue": "Son, we live in a world that has walls, and those walls have to be guarded by men with guns. Who's gonna do it? You?",
            "status_a": 7.5,
            "status_b": 10.0,
            "tension": 0.92,
            "target_x_a": 0.50,
            "target_x_b": 0.66,
            "gesture": "PACE_PROUDLY",
            "cam_zoom": 1.35,
            "cam_label": "JESSEP PACING TRUCK SHOT"
        },
        {
            "id": 10,
            "speaker": "AGENT_A",
            "dialogue": "Did you order the Code Red?!",
            "status_a": 9.9,
            "status_b": 8.5,
            "tension": 0.98,
            "target_x_a": 0.58,
            "target_x_b": 0.66,
            "gesture": "POINT_FINGER_LETHAL",
            "cam_zoom": 1.7,
            "cam_label": "FATAL INTERROGATION CLOSEUP"
        },
        {
            "id": 11,
            "speaker": "AGENT_B",
            "dialogue": "YOU'RE GODDAMN RIGHT I DID!",
            "status_a": 10.0,
            "status_b": 6.0,
            "tension": 1.0,
            "target_x_a": 0.58,
            "target_x_b": 0.66,
            "gesture": "FATAL_CONFESSION_FREEZE",
            "cam_zoom": 1.9,
            "cam_label": "CONFESSION IMPACT",
            "shake": 1.0
        },
        {
            "id": 12,
            "speaker": "AGENT_A",
            "dialogue": "Your Honor, these are the Marine guards. Have the witness taken into custody.",
            "status_a": 10.0,
            "status_b": 2.0,
            "tension": 0.40,
            "target_x_a": 0.38,
            "target_x_b": 0.66,
            "gesture": "TURN_BACK_CALM",
            "cam_zoom": 1.1,
            "cam_label": "WIDE CATHARSIS SHOT"
        }
    ]
}

SCENE_PULP_FICTION = {
    "title": "Pulp Fiction (1994)",
    "playwright": "Quentin Tarantino",
    "location": "Brett's Dilapidated Apartment - Morning",
    "prop_type": "APARTMENT_KAHUNA",
    "characters": {
        "AGENT_A": {
            "name": "JULES WINNFIELD",
            "role": "Righteous Hitman (Cold Intellectual Wrath)",
            "color": "#fbbf24",
            "voice_pitch": 0.92,
            "voice_rate": 1.02
        },
        "AGENT_B": {
            "name": "BRETT",
            "role": "Terrified College Kid / Small-Time Thief",
            "color": "#94a3b8",
            "voice_pitch": 1.30,
            "voice_rate": 1.18
        }
    },
    "props": [
        {"name": "Kitchen Table", "type": "TABLE", "x": 0.65, "y": 0.72},
        {"name": "Big Kahuna Burger & Sprite", "type": "FOOD", "x": 0.67, "y": 0.68},
        {"name": "Glowing Golden Briefcase", "type": "BRIEFCASE", "x": 0.42, "y": 0.72}
    ],
    "beats": [
        {
            "id": 1,
            "speaker": "AGENT_A",
            "dialogue": "Hey, kids. How y'all doing? Don't let us interrupt your breakfast.",
            "status_a": 8.5,
            "status_b": 3.0,
            "tension": 0.40,
            "target_x_a": 0.35,
            "target_x_b": 0.72,
            "gesture": "CALM_STRIDE",
            "cam_zoom": 1.0,
            "cam_label": "APARTMENT ENTRANCE WIDE"
        },
        {
            "id": 2,
            "speaker": "AGENT_B",
            "dialogue": "Jules, look... it's in the cupboard. The case is right there!",
            "status_a": 8.5,
            "status_b": 2.5,
            "tension": 0.50,
            "target_x_a": 0.38,
            "target_x_b": 0.72,
            "gesture": "TREMBLING_HANDS",
            "cam_zoom": 1.15,
            "cam_label": "BRETT PANIC CLOSEUP"
        },
        {
            "id": 3,
            "speaker": "AGENT_A",
            "dialogue": "Whatcha got there? Hamburgers? Big Kahuna Burger. That's that Hawaiian burger joint, right?",
            "status_a": 9.0,
            "status_b": 2.0,
            "tension": 0.58,
            "target_x_a": 0.48,
            "target_x_b": 0.72,
            "gesture": "INSPECT_BURGER",
            "cam_zoom": 1.3,
            "cam_label": "KAHUNA BURGER PUSH-IN"
        },
        {
            "id": 4,
            "speaker": "AGENT_B",
            "dialogue": "Yeah. It's... it's pretty good.",
            "status_a": 9.0,
            "status_b": 2.0,
            "tension": 0.62,
            "target_x_a": 0.48,
            "target_x_b": 0.72,
            "gesture": "SWALLOW_HARD",
            "cam_zoom": 1.35,
            "cam_label": "BRETT PROFILE"
        },
        {
            "id": 5,
            "speaker": "AGENT_A",
            "dialogue": "Mind if I have some of yours? This is a tasty burger! Vincent, you ever have a Big Kahuna Burger?",
            "status_a": 9.2,
            "status_b": 1.8,
            "tension": 0.68,
            "target_x_a": 0.52,
            "target_x_b": 0.70,
            "gesture": "BURGER_BITE",
            "cam_zoom": 1.45,
            "cam_label": "JULES SARDONIC SMILE"
        },
        {
            "id": 6,
            "speaker": "AGENT_A",
            "dialogue": "Mind if I have some of your tasty beverage to wash this down? Mmm... Sprite.",
            "status_a": 9.4,
            "status_b": 1.5,
            "tension": 0.75,
            "target_x_a": 0.54,
            "target_x_b": 0.70,
            "gesture": "STRAW_SLURP",
            "cam_zoom": 1.5,
            "cam_label": "STRAW SLURP TENSION"
        },
        {
            "id": 7,
            "speaker": "AGENT_A",
            "dialogue": "You know why we're here. Why don't you tell me where our boss's property is?",
            "status_a": 9.6,
            "status_b": 1.5,
            "tension": 0.82,
            "target_x_a": 0.55,
            "target_x_b": 0.68,
            "gesture": "ICE_COLD_STARE",
            "cam_zoom": 1.6,
            "cam_label": "THE SHIFT TO TERROR"
        },
        {
            "id": 8,
            "speaker": "AGENT_B",
            "dialogue": "It's in the cupboard! I swear, Marcellus Wallace is gonna get every cent back!",
            "status_a": 9.6,
            "status_b": 2.0,
            "tension": 0.86,
            "target_x_a": 0.55,
            "target_x_b": 0.68,
            "gesture": "PLEADING_TERROR",
            "cam_zoom": 1.65,
            "cam_label": "DESPERATE PLEA"
        },
        {
            "id": 9,
            "speaker": "AGENT_A",
            "dialogue": "Describe what Marcellus Wallace looks like!",
            "status_a": 9.8,
            "status_b": 1.5,
            "tension": 0.90,
            "target_x_a": 0.58,
            "target_x_b": 0.68,
            "gesture": "DRAW_PISTOL",
            "cam_zoom": 1.75,
            "cam_label": "PISTOL AIM POINT",
            "shake": 0.4
        },
        {
            "id": 10,
            "speaker": "AGENT_B",
            "dialogue": "What?!",
            "status_a": 9.8,
            "status_b": 1.2,
            "tension": 0.94,
            "target_x_a": 0.58,
            "target_x_b": 0.68,
            "gesture": "FLINCH_TERROR",
            "cam_zoom": 1.8,
            "cam_label": "BRETT WHAT"
        },
        {
            "id": 11,
            "speaker": "AGENT_A",
            "dialogue": "Say 'what' again! Say 'what' again, I dare you, I double dare you motherfucker, say what one more goddamn time!",
            "status_a": 10.0,
            "status_b": 1.0,
            "tension": 0.98,
            "target_x_a": 0.60,
            "target_x_b": 0.68,
            "gesture": "ROAR_AIM",
            "cam_zoom": 1.9,
            "cam_label": "DOUBLE DARE ROAR",
            "shake": 0.8
        },
        {
            "id": 12,
            "speaker": "AGENT_B",
            "dialogue": "He's black! He's bald! And he don't like to be fucked by anybody except Mrs. Wallace!",
            "status_a": 9.8,
            "status_b": 2.0,
            "tension": 0.95,
            "target_x_a": 0.58,
            "target_x_b": 0.68,
            "gesture": "DESPERATE_SCREAM",
            "cam_zoom": 1.7,
            "cam_label": "CONFESSION GASP"
        },
        {
            "id": 13,
            "speaker": "AGENT_A",
            "dialogue": "There's a passage I got memorized. Ezekiel 25:17.",
            "status_a": 10.0,
            "status_b": 1.0,
            "tension": 0.98,
            "target_x_a": 0.54,
            "target_x_b": 0.68,
            "gesture": "EZEKIEL_POSTURE",
            "cam_zoom": 1.85,
            "cam_label": "PROPHETIC ORATION"
        },
        {
            "id": 14,
            "speaker": "AGENT_A",
            "dialogue": "The path of the righteous man is beset on all sides by the iniquities of the selfish and the tyranny of evil men.",
            "status_a": 10.0,
            "status_b": 1.0,
            "tension": 0.99,
            "target_x_a": 0.54,
            "target_x_b": 0.68,
            "gesture": "EZEKIEL_MONOLOGUE_1",
            "cam_zoom": 1.9,
            "cam_label": "EZEKIEL CHANT 1"
        },
        {
            "id": 15,
            "speaker": "AGENT_A",
            "dialogue": "Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness.",
            "status_a": 10.0,
            "status_b": 1.0,
            "tension": 0.99,
            "target_x_a": 0.56,
            "target_x_b": 0.68,
            "gesture": "EZEKIEL_MONOLOGUE_2",
            "cam_zoom": 1.95,
            "cam_label": "EZEKIEL CHANT 2"
        },
        {
            "id": 16,
            "speaker": "AGENT_A",
            "dialogue": "And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy my brothers!",
            "status_a": 10.0,
            "status_b": 0.8,
            "tension": 1.0,
            "target_x_a": 0.58,
            "target_x_b": 0.68,
            "gesture": "ROAR_EZEKIEL_CLIMAX",
            "cam_zoom": 2.0,
            "cam_label": "FURIOUS ANGER CRESCENDO",
            "shake": 1.0
        },
        {
            "id": 17,
            "speaker": "AGENT_A",
            "dialogue": "AND YOU WILL KNOW MY NAME IS THE LORD WHEN I LAY MY VENGEANCE UPON THEE!",
            "status_a": 10.0,
            "status_b": 0.5,
            "tension": 1.0,
            "target_x_a": 0.60,
            "target_x_b": 0.68,
            "gesture": "GUNSHOT_EXECUTION",
            "cam_zoom": 2.1,
            "cam_label": "THE FATAL EXECUTION",
            "shake": 1.4
        }
    ]
}

SCENE_WHIPLASH = {
    "title": "Whiplash (2014)",
    "playwright": "Damien Chazelle",
    "location": "Studio Band Rehearsal Room - Nassau",
    "prop_type": "BAND_STUDIO",
    "characters": {
        "AGENT_A": {
            "name": "TERENCE FLETCHER",
            "role": "Symphonic Studio Conductor (Ruthless Perfectionist)",
            "color": "#ef4444",
            "voice_pitch": 0.85,
            "voice_rate": 1.05
        },
        "AGENT_B": {
            "name": "ANDREW NEIMAN",
            "role": "Obsessed First-Year Drummer",
            "color": "#38bdf8",
            "voice_pitch": 1.20,
            "voice_rate": 1.15
        }
    },
    "props": [
        {"name": "Snare Drum & Ride Cymbal", "type": "DRUMS", "x": 0.72, "y": 0.72},
        {"name": "Conductor Music Stand", "type": "STAND", "x": 0.38, "y": 0.72}
    ],
    "beats": [
        {
            "id": 1,
            "speaker": "AGENT_A",
            "dialogue": "Caravan. Bar one-fifteen. Five, six, and...",
            "status_a": 9.0,
            "status_b": 5.0,
            "tension": 0.45,
            "target_x_a": 0.36,
            "target_x_b": 0.72,
            "gesture": "CONDUCTING_HANDS",
            "cam_zoom": 1.0,
            "cam_label": "STUDIO WIDE"
        },
        {
            "id": 2,
            "speaker": "AGENT_A",
            "dialogue": "Stop. Neiman, you're rushing.",
            "status_a": 9.5,
            "status_b": 4.5,
            "tension": 0.65,
            "target_x_a": 0.42,
            "target_x_b": 0.72,
            "gesture": "RAISE_FIST_HALT",
            "cam_zoom": 1.25,
            "cam_label": "HALT TENSION",
            "shake": 0.3
        },
        {
            "id": 3,
            "speaker": "AGENT_B",
            "dialogue": "Sorry, Mr. Fletcher. Let me count it off.",
            "status_a": 9.2,
            "status_b": 3.8,
            "tension": 0.70,
            "target_x_a": 0.45,
            "target_x_b": 0.72,
            "gesture": "TENSE_DRUMSTICKS",
            "cam_zoom": 1.35,
            "cam_label": "DRUMMER ANXIETY"
        },
        {
            "id": 4,
            "speaker": "AGENT_A",
            "dialogue": "Not quite my tempo. Were you rushing or were you dragging?!",
            "status_a": 10.0,
            "status_b": 3.0,
            "tension": 0.88,
            "target_x_a": 0.58,
            "target_x_b": 0.72,
            "gesture": "LEAN_INTO_FACE",
            "cam_zoom": 1.7,
            "cam_label": "FACE-TO-FACE INTIMIDATION",
            "shake": 0.6
        },
        {
            "id": 5,
            "speaker": "AGENT_B",
            "dialogue": "I... I don't know...",
            "status_a": 10.0,
            "status_b": 1.8,
            "tension": 0.94,
            "target_x_a": 0.58,
            "target_x_b": 0.72,
            "gesture": "TREMBLING_HEAD_DOWN",
            "cam_zoom": 1.85,
            "cam_label": "PSYCHOLOGICAL BREAKDOWN"
        },
        {
            "id": 6,
            "speaker": "AGENT_A",
            "dialogue": "There are no two words in the English language more harmful than 'good job.' Start again!",
            "status_a": 10.0,
            "status_b": 2.2,
            "tension": 0.98,
            "target_x_a": 0.50,
            "target_x_b": 0.72,
            "gesture": "POINT_DRUMSTICKS",
            "cam_zoom": 1.6,
            "cam_label": "FLETCHER PHILOSOPHY",
            "shake": 0.8
        }
    ]
}

SCENE_THE_DARK_KNIGHT = {
    "title": "The Dark Knight (2008)",
    "playwright": "Jonathan & Christopher Nolan",
    "location": "Gotham Central Police Interrogation Room",
    "prop_type": "INTERROGATION",
    "characters": {
        "AGENT_A": {
            "name": "BATMAN",
            "role": "Vigilante (Relentless Unstoppable Force)",
            "color": "#38bdf8",
            "voice_pitch": 0.75,
            "voice_rate": 0.95
        },
        "AGENT_B": {
            "name": "THE JOKER",
            "role": "Agent of Chaos (Unshakable Psychological Status)",
            "color": "#a855f7",
            "voice_pitch": 1.25,
            "voice_rate": 1.15
        }
    },
    "props": [
        {"name": "Steel Table", "type": "TABLE", "x": 0.55, "y": 0.72},
        {"name": "Overhead Low Hanging Bulb", "type": "LIGHT", "x": 0.55, "y": 0.40}
    ],
    "beats": [
        {
            "id": 1,
            "speaker": "AGENT_A",
            "dialogue": "Where are they?!",
            "status_a": 8.5,
            "status_b": 9.5,
            "tension": 0.70,
            "target_x_a": 0.45,
            "target_x_b": 0.68,
            "gesture": "SLAM_TABLE",
            "cam_zoom": 1.3,
            "cam_label": "TABLE SLAM IMPACT",
            "shake": 0.6
        },
        {
            "id": 2,
            "speaker": "AGENT_B",
            "dialogue": "You have nothing, nothing to threaten me with. Nothing to do with all your strength.",
            "status_a": 7.5,
            "status_b": 10.0,
            "tension": 0.85,
            "target_x_a": 0.45,
            "target_x_b": 0.68,
            "gesture": "LAUGH_LEAN",
            "cam_zoom": 1.5,
            "cam_label": "JOKER PSYCHOLOGICAL CLOSEUP"
        },
        {
            "id": 3,
            "speaker": "AGENT_A",
            "dialogue": "Where is Rachel?!",
            "status_a": 9.0,
            "status_b": 9.5,
            "tension": 0.92,
            "target_x_a": 0.55,
            "target_x_b": 0.68,
            "gesture": "GRAB_COLLAR",
            "cam_zoom": 1.7,
            "cam_label": "PHYSICAL VIOLENCE TIGHT SHOT",
            "shake": 0.5
        },
        {
            "id": 4,
            "speaker": "AGENT_B",
            "dialogue": "Killing is a choice. You have to choose between one life or the other. Your friend the DA, or his blushing bride-to-be.",
            "status_a": 6.0,
            "status_b": 10.0,
            "tension": 0.98,
            "target_x_a": 0.52,
            "target_x_b": 0.68,
            "gesture": "DELIGHTED_CHAOS",
            "cam_zoom": 1.8,
            "cam_label": "THE DILEMMA REVEAL",
            "shake": 0.4
        },
        {
            "id": 5,
            "speaker": "AGENT_A",
            "dialogue": "WHERE ARE THEY?!",
            "status_a": 9.5,
            "status_b": 9.8,
            "tension": 1.00,
            "target_x_a": 0.58,
            "target_x_b": 0.68,
            "gesture": "ROAR",
            "cam_zoom": 1.9,
            "cam_label": "CLIMAX SHOUT",
            "shake": 0.8
        },
        {
            "id": 6,
            "speaker": "AGENT_B",
            "dialogue": "Which one are you going after? He's at 250 52nd Street, and she's on Avenue X.",
            "status_a": 8.0,
            "status_b": 10.0,
            "tension": 0.85,
            "target_x_a": 0.35,
            "target_x_b": 0.68,
            "gesture": "CACKLE_SOLITARY",
            "cam_zoom": 1.2,
            "cam_label": "BATMAN RUNAWAY PULLOUT"
        }
    ]
}

SCENE_THE_SOCIAL_NETWORK = {
    "title": "The Social Network (2010)",
    "playwright": "Aaron Sorkin",
    "location": "Palo Alto Facebook Office - Rainy Afternoon",
    "prop_type": "SILICON_VALLEY",
    "characters": {
        "AGENT_A": {
            "name": "EDUARDO SAVERIN",
            "role": "Cofounder / CFO (Betrayed)",
            "color": "#f97316",
            "voice_pitch": 1.05,
            "voice_rate": 1.15
        },
        "AGENT_B": {
            "name": "MARK ZUCKERBERG",
            "role": "CEO / Founder (Detached)",
            "color": "#38bdf8",
            "voice_pitch": 0.90,
            "voice_rate": 1.20
        }
    },
    "props": [
        {"name": "Standing Desk", "type": "TABLE", "x": 0.70, "y": 0.72}
    ],
    "beats": [
        {
            "id": 1,
            "speaker": "AGENT_A",
            "dialogue": "Mark! You set me up.",
            "status_a": 7.0,
            "status_b": 7.0,
            "tension": 0.60,
            "target_x_a": 0.30,
            "target_x_b": 0.72,
            "gesture": "MARCH_IN",
            "cam_zoom": 1.0,
            "cam_label": "ENTRANCE WIDE"
        },
        {
            "id": 2,
            "speaker": "AGENT_B",
            "dialogue": "A million dollars isn't cool. You know what's cool? A billion dollars.",
            "status_a": 6.5,
            "status_b": 8.5,
            "tension": 0.70,
            "target_x_a": 0.38,
            "target_x_b": 0.72,
            "gesture": "SLIGHT_TILT",
            "cam_zoom": 1.25,
            "cam_label": "ZUCKERBERG MONOTONE TIGHT"
        },
        {
            "id": 3,
            "speaker": "AGENT_A",
            "dialogue": "You issued twenty-four million new shares of stock... and diluted my shares down to 0.03 percent!",
            "status_a": 8.5,
            "status_b": 7.5,
            "tension": 0.85,
            "target_x_a": 0.50,
            "target_x_b": 0.70,
            "gesture": "SLAM_TABLE",
            "cam_zoom": 1.45,
            "cam_label": "DESK CONFRONTATION",
            "shake": 0.4
        },
        {
            "id": 4,
            "speaker": "AGENT_B",
            "dialogue": "You signed the papers, Eduardo.",
            "status_a": 8.0,
            "status_b": 8.5,
            "tension": 0.88,
            "target_x_a": 0.50,
            "target_x_b": 0.70,
            "gesture": "MONOTONE_GLARE",
            "cam_zoom": 1.5,
            "cam_label": "EYE CONTACT LOCK"
        },
        {
            "id": 5,
            "speaker": "AGENT_A",
            "dialogue": "My name was on the masthead! I was your only friend! You had ONE friend!",
            "status_a": 9.8,
            "status_b": 4.5,
            "tension": 0.98,
            "target_x_a": 0.58,
            "target_x_b": 0.70,
            "gesture": "SHATTER_LAPTOP",
            "cam_zoom": 1.75,
            "cam_label": "LAPTOP SMASH IMPACT",
            "shake": 0.8
        },
        {
            "id": 6,
            "speaker": "AGENT_A",
            "dialogue": "You better lawyer up, asshole. Because I'm not coming back for thirty percent. I'm coming back for everything.",
            "status_a": 10.0,
            "status_b": 3.0,
            "tension": 0.90,
            "target_x_a": 0.54,
            "target_x_b": 0.74,
            "gesture": "POINT_EXIT",
            "cam_zoom": 1.3,
            "cam_label": "EXIT PULLBACK"
        }
    ]
}

ALL_SCENES = {
    "pulp_fiction": SCENE_PULP_FICTION,
    "whiplash": SCENE_WHIPLASH,
    "a_few_good_men": SCENE_A_FEW_GOOD_MEN,
    "dark_knight": SCENE_THE_DARK_KNIGHT,
    "social_network": SCENE_THE_SOCIAL_NETWORK
}
