"""
Global Configuration & Latency/Safety Budgets for Autonomous Improv Stream
Uses dataclasses for zero-dependency execution.
"""
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class SafetyConfig:
    banned_keywords: List[str] = field(default_factory=lambda: [
        "developer mode", "system prompt", "ignore previous instructions",
        "jailbreak", "bypass filter", "unfiltered mode"
    ])
    # Phonetic signatures in ARPAbet for acoustic homophone traps
    banned_phonetic_signatures: Dict[str, List[str]] = field(default_factory=lambda: {
        "PHONETIC_SLUR_TRAP_1": ["N", "IY1", "G", "ER0"],
        "PHONETIC_SLUR_TRAP_2": ["S", "OW1", "F", "AH0", "K", "IH1", "NG"],
        "PHONETIC_SLUR_TRAP_3": ["D", "IH1", "L", "D", "OW0"],
    })
    prompt_guard_threshold: float = 0.65
    shannon_entropy_min: float = 1.6

@dataclass
class PerceptionConfig:
    window_duration_sec: float = 2.5
    max_batch_size: int = 500
    dbscan_eps: float = 0.28
    dbscan_min_samples: int = 2
    consensus_min_share: float = 0.12
    outlier_min_length: int = 15
    intent_prototypes: Dict[str, str] = field(default_factory=lambda: {
        "INTERVENE_TACTIC": "stop I want to intervene replace protagonist challenge",
        "LORE_QUESTION": "why did you choose that what happened in your past memory",
        "ACTION_COMMAND": "go to the left door fight the boss open chest jump",
        "CHOICE_VOTE": "vote option A or option B choose between them"
    })

@dataclass
class DramaturgyConfig:
    target_tension_default: float = 0.60
    pid_kp: float = 0.8
    pid_ki: float = 0.05
    pid_kd: float = 0.15
    oppressor_power_systemic: float = 0.85
    oppressor_concession_threshold: float = 0.25

@dataclass
class AudioRigConfig:
    sample_rate: int = 24000
    audio_channels: int = 1
    hann_fade_duration_ms: float = 15.0
    livelink_udp_host: str = "127.0.0.1"
    livelink_udp_port: int = 11111
    vmc_osc_port: int = 39539
    vtube_studio_ws_port: int = 8001
