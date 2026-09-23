"""
High-Performance Recursive PII and Credential Scrubbing Middleware.
Enforces GDPR / DPDP compliance by scrubbing sensitive data before persistence or export.
"""
import re
from typing import Any, Dict, List, Set, Union
import hashlib

SENSITIVE_KEY_PATTERNS: Set[str] = {
    "password", "passwd", "secret", "token", "apikey", "api_key", "access_token",
    "auth", "authorization", "bearer", "cookie", "private_key", "privatekey",
    "ssn", "social_security", "credit_card", "creditcard", "cvv", "card_number",
    "aadhaar", "passport", "email", "phone", "phone_number", "mobile"
}

# Regex patterns for values that look like API keys or tokens
REGEX_TOKEN = re.compile(r"^(?:sk-[a-zA-Z0-9_-]{20,}|ghp_[a-zA-Z0-9]{20,}|eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}|Bearer\s+[a-zA-Z0-9_\-\.]+)", re.IGNORECASE)
REGEX_EMAIL = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
REGEX_PHONE = re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b")

class SanitizePolicy:
    REDACTED_TEXT = "[REDACTED]"
    MASK_HASH = True

    @classmethod
    def mask_hash(cls, val: str) -> str:
        """Masks value but preserves deterministic hash prefix for ML/debugging correlation."""
        h = hashlib.sha256(val.encode("utf-8")).hexdigest()[:8]
        return f"[REDACTED:sha256:{h}]"

def sanitize_value(key: str, val: Any) -> Any:
    """
    Sanitizes a single value based on key name and value pattern.
    """
    if val is None:
        return None

    # Check key name
    k_lower = key.lower().replace("-", "_")
    for pattern in SENSITIVE_KEY_PATTERNS:
        if pattern in k_lower:
            return SanitizePolicy.mask_hash(str(val)) if SanitizePolicy.MASK_HASH else SanitizePolicy.REDACTED_TEXT

    # Check string patterns
    if isinstance(val, str):
        if REGEX_TOKEN.search(val):
            return SanitizePolicy.mask_hash(val)
        if REGEX_EMAIL.search(val):
            val = REGEX_EMAIL.sub("[REDACTED_EMAIL]", val)
        if REGEX_PHONE.search(val):
            val = REGEX_PHONE.sub("[REDACTED_PHONE]", val)
        return val

    # Recurse on collections
    if isinstance(val, dict):
        return sanitize_payload(val)
    if isinstance(val, (list, tuple, set)):
        return [sanitize_value(key, item) for item in val]

    return val

def sanitize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively scrubs a dictionary of all sensitive keys and values.
    """
    if not isinstance(payload, dict):
        return payload

    clean = {}
    for k, v in payload.items():
        clean[k] = sanitize_value(k, v)
    return clean
