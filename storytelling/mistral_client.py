"""
Resilient Rotating Multi-Key Mistral AI Client.
Implements:
- Thread-safe Round-Robin Key Rotation across 3 keys
- Automatic 429 Rate-Limit detection with exponential backoff & dynamic cooldown
- Circuit breaker per key with failover cascading
- Zero external dependencies using standard library urllib.request
- Full distributed tracing and telemetry integration with the Observability Engine
"""
import os
import time
import json
import threading
import urllib.request
import urllib.error
from typing import List, Dict, Any, Optional, Tuple

from observability import LOGGER, trace_span

DEFAULT_MISTRAL_KEYS = [
    "wq0rN6hcd14dGMsgb3GsttNvClcQiPDB",
    "A3ZfrQo2f7k1W1bHRd9uoYskM6Wdz07L",
    "IfVtFz6JhaF3mvbh4fNTcNh5eShvpj4k"
]

class MistralKeyEntry:
    def __init__(self, key: str, index: int):
        self.key = key.strip()
        self.index = index
        self.masked_id = f"key_{index + 1}[{self.key[:4]}...{self.key[-4:]}]"
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.total_tokens = 0
        self.cooldown_until: float = 0.0
        self.consecutive_429s = 0

    @property
    def is_available(self) -> bool:
        return time.time() >= self.cooldown_until

    def mark_rate_limited(self, backoff_seconds: float = 30.0):
        self.consecutive_429s += 1
        # Exponential backoff capped at 120s
        multiplier = min(4, 2 ** (self.consecutive_429s - 1))
        duration = backoff_seconds * multiplier
        self.cooldown_until = time.time() + duration
        self.failed_requests += 1

    def mark_success(self, tokens_used: int = 0):
        self.successful_requests += 1
        self.consecutive_429s = 0
        self.cooldown_until = 0.0
        self.total_tokens += tokens_used

    def mark_error(self):
        self.failed_requests += 1

    def to_dict(self) -> Dict[str, Any]:
        now = time.time()
        remaining_cooldown = max(0.0, round(self.cooldown_until - now, 1))
        return {
            "index": self.index,
            "masked_id": self.masked_id,
            "is_available": self.is_available,
            "remaining_cooldown_sec": remaining_cooldown,
            "total_requests": self.total_requests,
            "successful_requests": self.successful_requests,
            "failed_requests": self.failed_requests,
            "total_tokens": self.total_tokens
        }


class MistralKeyPool:
    """Thread-safe round-robin key manager with health tracking and failover."""
    def __init__(self, keys: Optional[List[str]] = None):
        raw_keys = keys or DEFAULT_MISTRAL_KEYS
        self.entries = [MistralKeyEntry(k, idx) for idx, k in enumerate(raw_keys) if k.strip()]
        self._lock = threading.Lock()
        self._cursor = 0

    def get_next_key(self) -> Tuple[MistralKeyEntry, int]:
        """Returns the next healthy key using round-robin. Falls back to shortest cooldown if all busy."""
        with self._lock:
            n = len(self.entries)
            if n == 0:
                raise ValueError("No Mistral API keys configured in pool.")

            # First pass: find an immediately available key starting from cursor
            for offset in range(n):
                idx = (self._cursor + offset) % n
                entry = self.entries[idx]
                if entry.is_available:
                    self._cursor = (idx + 1) % n
                    entry.total_requests += 1
                    return entry, idx

            # Second pass: all are on cooldown, pick the one with earliest cooldown expiry
            soonest_entry = min(self.entries, key=lambda e: e.cooldown_until)
            soonest_entry.total_requests += 1
            return soonest_entry, soonest_entry.index

    def get_status(self) -> List[Dict[str, Any]]:
        with self._lock:
            return [e.to_dict() for e in self.entries]


class MistralRotatingClient:
    """
    Applied AI Client for Mistral Chat Completions with:
    - Automatic multi-key rotation
    - Guaranteed valid JSON structured output
    - Telemetry metrics & trace propagation
    """
    ENDPOINT = "https://api.mistral.ai/v1/chat/completions"

    def __init__(self, pool: Optional[MistralKeyPool] = None, default_model: str = "open-mistral-7b"):
        self.pool = pool or MistralKeyPool()
        self.default_model = default_model

    def complete(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1024,
        json_mode: bool = True,
        max_attempts: int = 3
    ) -> Dict[str, Any]:
        """
        Executes a chat completion across rotating keys with automatic retry on 429 / transient 5xx.
        """
        chosen_model = model or self.default_model
        payload_data = {
            "model": chosen_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        if json_mode:
            payload_data["response_format"] = {"type": "json_object"}

        body_bytes = json.dumps(payload_data).encode("utf-8")
        last_error = None

        with trace_span("mistral_llm_inference", service="mistral-client", attributes={"model": chosen_model, "json_mode": json_mode}):
            for attempt in range(max_attempts):
                entry, key_idx = self.pool.get_next_key()
                req = urllib.request.Request(
                    self.ENDPOINT,
                    data=body_bytes,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {entry.key}",
                        "User-Agent": "ALIPS-Theatrical-Engine/1.0"
                    }
                )

                start_t = time.perf_counter()
                try:
                    with urllib.request.urlopen(req, timeout=12) as response:
                        duration_ms = (time.perf_counter() - start_t) * 1000.0
                        raw_resp = response.read().decode("utf-8")
                        resp_json = json.loads(raw_resp)

                        # Extract usage
                        usage = resp_json.get("usage", {})
                        total_tokens = usage.get("total_tokens", 0)
                        entry.mark_success(tokens_used=total_tokens)

                        LOGGER.increment("mistral.requests.success", labels={"key_index": str(key_idx), "model": chosen_model})
                        LOGGER.timing("mistral.latency_ms", duration_ms, labels={"key_index": str(key_idx)})

                        content = resp_json["choices"][0]["message"]["content"]
                        parsed_content = json.loads(content) if json_mode else content

                        return {
                            "success": True,
                            "content": parsed_content,
                            "raw_text": content,
                            "key_used": entry.masked_id,
                            "key_index": key_idx,
                            "duration_ms": round(duration_ms, 2),
                            "model": chosen_model,
                            "tokens": total_tokens
                        }

                except urllib.error.HTTPError as http_err:
                    duration_ms = (time.perf_counter() - start_t) * 1000.0
                    status_code = http_err.code
                    err_msg = http_err.read().decode("utf-8", errors="ignore")

                    if status_code == 429:
                        entry.mark_rate_limited(backoff_seconds=20.0)
                        LOGGER.warn(
                            "mistral.rate_limit_exceeded",
                            service="mistral-client",
                            payload={"key_index": key_idx, "error": err_msg, "duration_ms": duration_ms}
                        )
                        LOGGER.increment("mistral.requests.rate_limited", labels={"key_index": str(key_idx)})
                    else:
                        entry.mark_error()
                        LOGGER.error(
                            "mistral.http_error",
                            service="mistral-client",
                            payload={"key_index": key_idx, "status": status_code, "error": err_msg}
                        )
                    last_error = f"HTTP {status_code}: {err_msg}"
                    time.sleep(0.3) # Fast retry cadence across alternative keys

                except Exception as ex:
                    entry.mark_error()
                    LOGGER.error(
                        "mistral.network_exception",
                        service="mistral-client",
                        payload={"key_index": key_idx, "error": str(ex)}
                    )
                    last_error = str(ex)
                    time.sleep(0.3)

        return {
            "success": False,
            "error": last_error or "All Mistral keys exhausted or unavailable.",
            "content": None
        }

# Global Singleton
MISTRAL_CLIENT = MistralRotatingClient()
