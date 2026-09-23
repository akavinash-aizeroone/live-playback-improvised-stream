"""
Screenplay Library: Iconic Cinematic & Theatrical Showdowns
Includes exact dialogue, status coordinates, kinematic stage targets,
and Augusto Boal intervention checkpoints.
"""

SCENE_A_FEW_GOOD_MEN = {
    "title": "A Few Good Men (1992)",
    "playwright": "Aaron Sorkin",
    "location": "Guantanamo Bay Court-Martial Courtroom",
    "characters": {
        "AGENT_A": {
            "name": "LT. DANIEL KAFFEE",
            "role": "Lead Defense Counsel (Prosecuting the Colonel)",
            "color": "#38bdf8",
            "voice_pitch": 1.1,
            "voice_rate": 1.05
        },
        "AGENT_B": {
            "name": "COL. NATHAN R. JESSEP",
            "role": "Commander, Marine Barracks Guantanamo",
            "color": "#f87171",
            "voice_pitch": 0.85,
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
            "target_x_a": 0.35,
            "target_x_b": 0.75,
            "gesture": "POINT_LEGAL_PAD"
        },
        {
            "id": 2,
            "speaker": "AGENT_B",
            "dialogue": "You don't have to answer that question!",
            "status_a": 7.0,
            "status_b": 9.8,
            "tension": 0.62,
            "target_x_a": 0.35,
            "target_x_b": 0.75,
            "gesture": "CHEST_PUFF"
        },
        {
            "id": 3,
            "speaker": "AGENT_A",
            "dialogue": "Your Honor, I have the right to question the witness on this issue!",
            "status_a": 7.8,
            "status_b": 9.5,
            "tension": 0.70,
            "target_x_a": 0.45,
            "target_x_b": 0.75,
            "gesture": "STRIDE_FORWARD"
        },
        {
            "id": 4,
            "speaker": "AGENT_B",
            "dialogue": "I'll answer the question. You want answers?",
            "status_a": 8.0,
            "status_b": 9.5,
            "tension": 0.75,
            "target_x_a": 0.48,
            "target_x_b": 0.72,
            "gesture": "LEAN_OVER_RAIL"
        },
        {
            "id": 5,
            "speaker": "AGENT_A",
            "dialogue": "I think I'm entitled to them.",
            "status_a": 8.5,
            "status_b": 9.2,
            "tension": 0.80,
            "target_x_a": 0.52,
            "target_x_b": 0.70,
            "gesture": "STEADY_STANCE"
        },
        {
            "id": 6,
            "speaker": "AGENT_B",
            "dialogue": "You want answers?!",
            "status_a": 8.5,
            "status_b": 9.8,
            "tension": 0.88,
            "target_x_a": 0.52,
            "target_x_b": 0.68,
            "gesture": "STEP_OUT_OF_STAND"
        },
        {
            "id": 7,
            "speaker": "AGENT_A",
            "dialogue": "I WANT THE TRUTH!",
            "status_a": 9.5,
            "status_b": 9.8,
            "tension": 0.95,
            "target_x_a": 0.56,
            "target_x_b": 0.68,
            "gesture": "BOTH_ARMS_FORWARD"
        },
        {
            "id": 8,
            "speaker": "AGENT_B",
            "dialogue": "YOU CAN'T HANDLE THE TRUTH!",
            "status_a": 8.0,
            "status_b": 10.0,
            "tension": 1.0,
            "target_x_a": 0.54,
            "target_x_b": 0.66,
            "gesture": "ROAR_EXPAND_SCALE"
        },
        {
            "id": 9,
            "speaker": "AGENT_B",
            "dialogue": "Son, we live in a world that has walls, and those walls have to be guarded by men with guns. Who's gonna do it? You?",
            "status_a": 7.5,
            "status_b": 10.0,
            "tension": 0.92,
            "target_x_a": 0.50,
            "target_x_b": 0.64,
            "gesture": "PACE_PROUDLY"
        },
        {
            "id": 10,
            "speaker": "AGENT_A",
            "dialogue": "Did you order the Code Red?!",
            "status_a": 9.8,
            "status_b": 8.5,
            "tension": 0.98,
            "target_x_a": 0.58,
            "target_x_b": 0.64,
            "gesture": "POINT_FINGER_LETHAL"
        },
        {
            "id": 11,
            "speaker": "AGENT_B",
            "dialogue": "YOU'RE GODDAMN RIGHT I DID!",
            "status_a": 9.9,
            "status_b": 6.0,
            "tension": 1.0,
            "target_x_a": 0.58,
            "target_x_b": 0.64,
            "gesture": "FATAL_CONFESSION_FREEZE"
        },
        {
            "id": 12,
            "speaker": "AGENT_A",
            "dialogue": "Your Honor, these are the Marine guards. Have the witness taken into custody.",
            "status_a": 10.0,
            "status_b": 2.0,
            "tension": 0.40,
            "target_x_a": 0.38,
            "target_x_b": 0.64,
            "gesture": "TURN_BACK_CALM"
        }
    ]
}

SCENE_THE_SOCIAL_NETWORK = {
    "title": "The Social Network (2010)",
    "playwright": "Aaron Sorkin",
    "location": "Palo Alto Facebook Office - Rainy Afternoon",
    "characters": {
        "AGENT_A": {
            "name": "EDUARDO SAVERIN",
            "role": "Cofounder / CFO (Betrayed)",
            "color": "#f97316",
            "voice_pitch": 1.0,
            "voice_rate": 1.1
        },
        "AGENT_B": {
            "name": "MARK ZUCKERBERG",
            "role": "CEO / Founder (Detached)",
            "color": "#38bdf8",
            "voice_pitch": 0.9,
            "voice_rate": 1.15
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
            "target_x_a": 0.35,
            "target_x_b": 0.70,
            "gesture": "STRIDE_INTO_ROOM"
        },
        {
            "id": 2,
            "speaker": "AGENT_B",
            "dialogue": "A million dollars isn't cool. You know what's cool? A billion dollars.",
            "status_a": 6.5,
            "status_b": 8.5,
            "tension": 0.68,
            "target_x_a": 0.40,
            "target_x_b": 0.70,
            "gesture": "SLIGHT_HEAD_TILT"
        },
        {
            "id": 3,
            "speaker": "AGENT_A",
            "dialogue": "You issued twenty-four million new shares of stock... and diluted my shares down to 0.03 percent!",
            "status_a": 8.5,
            "status_b": 7.5,
            "tension": 0.82,
            "target_x_a": 0.52,
            "target_x_b": 0.68,
            "gesture": "SLAM_DESK"
        },
        {
            "id": 4,
            "speaker": "AGENT_B",
            "dialogue": "You signed the papers, Eduardo.",
            "status_a": 8.0,
            "status_b": 8.5,
            "tension": 0.85,
            "target_x_a": 0.52,
            "target_x_b": 0.68,
            "gesture": "MONOTONE_GLARE"
        },
        {
            "id": 5,
            "speaker": "AGENT_A",
            "dialogue": "My name was on the masthead! I was your only friend! You had ONE friend!",
            "status_a": 9.5,
            "status_b": 5.0,
            "tension": 0.98,
            "target_x_a": 0.58,
            "target_x_b": 0.68,
            "gesture": "BREAK_LAPTOP_SWING"
        },
        {
            "id": 6,
            "speaker": "AGENT_A",
            "dialogue": "You better lawyer up, asshole. Because I'm not coming back for thirty percent. I'm coming back for everything.",
            "status_a": 10.0,
            "status_b": 3.0,
            "tension": 0.90,
            "target_x_a": 0.55,
            "target_x_b": 0.72,
            "gesture": "POINT_EXIT"
        }
    ]
}

ALL_SCENES = {
    "a_few_good_men": SCENE_A_FEW_GOOD_MEN,
    "social_network": SCENE_THE_SOCIAL_NETWORK
}
