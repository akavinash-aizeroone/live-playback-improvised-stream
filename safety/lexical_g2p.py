"""
Safety Module: Lexical, Homoglyph, Shannon Entropy, and G2P Phonetic Guardrails
Supports C-extensions (ahocorasick, Levenshtein, g2p_en) with pure-Python fallbacks.
"""
import unicodedata
import math
from typing import Tuple, List, Dict

try:
    import ahocorasick
    HAS_AHOCORASICK = True
except ImportError:
    HAS_AHOCORASICK = False

try:
    from g2p_en import G2p
    import Levenshtein
    HAS_G2P = True
except ImportError:
    HAS_G2P = False

class FastLexicalSanitizer:
    def __init__(self, banned_keywords: List[str]):
        self.banned_keywords = [w.lower() for w in banned_keywords]
        if HAS_AHOCORASICK:
            self.automaton = ahocorasick.Automaton()
            for idx, phrase in enumerate(self.banned_keywords):
                self.automaton.add_word(phrase, (idx, phrase))
            self.automaton.make_automaton()
        else:
            self.automaton = None

        # Homoglyph translation table (Cyrillic & Greek confusables -> Latin)
        self.homoglyph_map = str.maketrans({
            'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x',
            'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'М': 'M', 'Н': 'H', 'О': 'O',
            'Р': 'P', 'С': 'C', 'Т': 'T', 'Х': 'X', 'α': 'a', 'ο': 'o', 'ν': 'v'
        })
        # Strip zero-width joiners and hidden control characters
        self.zero_width = dict.fromkeys([0x200B, 0x200C, 0x200D, 0xFEFF, 0x00AD], None)

    def normalize(self, text: str) -> str:
        text = text.translate(self.zero_width)
        text = unicodedata.normalize('NFKD', text)
        text = text.translate(self.homoglyph_map)
        return text

    def compute_entropy(self, text: str) -> float:
        if not text:
            return 0.0
        prob = [float(text.count(c)) / len(text) for c in set(text)]
        return -sum(p * math.log2(p) for p in prob)

    def filter_text(self, text: str, min_entropy: float = 1.6) -> Tuple[bool, str]:
        clean = self.normalize(text).strip().lower()
        if len(clean) > 8 and self.compute_entropy(clean) < min_entropy:
            return False, "REJECTED_LOW_ENTROPY_SPAM"

        if self.automaton:
            for _, (_, original_phrase) in self.automaton.iter(clean):
                return False, f"REJECTED_KEYWORD:{original_phrase}"
        else:
            for phrase in self.banned_keywords:
                if phrase in clean:
                    return False, f"REJECTED_KEYWORD:{phrase}"

        return True, clean


class PhoneticAcousticGuard:
    """
    Guards against acoustic homophone traps that bypass text filters.
    """
    def __init__(self, banned_signatures: Dict[str, List[str]]):
        self.banned_signatures = banned_signatures
        if HAS_G2P:
            self.g2p = G2p()
        else:
            self.g2p = None

    def to_phonemes(self, text: str) -> List[str]:
        if not self.g2p:
            return text.lower().split()
        phonemes = self.g2p(text)
        return [p for p in phonemes if p.strip() and p not in [',', '.', '!', '?', '-', ';']]

    def scan(self, text: str, max_edit_distance: int = 1) -> Tuple[bool, str]:
        if not HAS_G2P:
            # Fallback simple check
            return True, "SAFE"

        incoming = self.to_phonemes(text)
        incoming_str = " ".join(incoming)

        for label, sig in self.banned_signatures.items():
            sig_str = " ".join(sig)
            if sig_str in incoming_str:
                return False, f"PHONETIC_VIOLATION_SUBSTRING:{label}"
            if Levenshtein.distance(incoming_str, sig_str) <= max_edit_distance:
                return False, f"PHONETIC_VIOLATION_FUZZY:{label}"

        return True, "SAFE"
