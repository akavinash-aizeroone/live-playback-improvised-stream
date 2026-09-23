"""
Storytelling Package: Applied AI Theatrical & Narrative Architecture.
Integrates Keith Johnstone (Improv & Status), Augusto Boal (Forum Theatre),
Jonathan Fox (Playback Theatre), and Robert McKee (Dramatic Value Shifts)
powered by a multi-key rotating Mistral AI cluster.
"""
from storytelling.mistral_client import MistralKeyPool, MistralRotatingClient, MISTRAL_CLIENT
from storytelling.dramaturgy_ai import (
    TheatricalTechnique,
    DramaturgyAIEngine,
    THEATRICAL_ENGINE
)

__all__ = [
    "MistralKeyPool",
    "MistralRotatingClient",
    "MISTRAL_CLIENT",
    "TheatricalTechnique",
    "DramaturgyAIEngine",
    "THEATRICAL_ENGINE"
]
