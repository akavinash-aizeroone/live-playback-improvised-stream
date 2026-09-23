"""
OpenTelemetry-Compatible Structured Telemetry Schema.
Standardized across logs, metrics, and distributed traces.
Adheres to W3C Trace Context and CloudEvents specifications.
Supports integer enum normalization and 16-byte binary UUIDs for zero-deletion SQLite density.
"""
from dataclasses import dataclass, field, asdict
from enum import IntEnum, Enum
from typing import Dict, Any, Optional, Union
import datetime
import uuid
import time

class LogLevel(str, Enum):
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"
    CRITICAL = "FATAL" # alias for backward compatibility

class LogLevelInt(IntEnum):
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    FATAL = 5

LEVEL_STR_TO_INT = {
    "TRACE": LogLevelInt.TRACE,
    "DEBUG": LogLevelInt.DEBUG,
    "INFO": LogLevelInt.INFO,
    "WARN": LogLevelInt.WARN,
    "ERROR": LogLevelInt.ERROR,
    "FATAL": LogLevelInt.FATAL,
    "CRITICAL": LogLevelInt.FATAL
}

LEVEL_INT_TO_STR = {
    LogLevelInt.TRACE: "TRACE",
    LogLevelInt.DEBUG: "DEBUG",
    LogLevelInt.INFO: "INFO",
    LogLevelInt.WARN: "WARN",
    LogLevelInt.ERROR: "ERROR",
    LogLevelInt.FATAL: "FATAL"
}

class LogStatusInt(IntEnum):
    SUCCESS = 0
    FAILURE = 1
    TIMEOUT = 2
    SKIPPED = 3

STATUS_STR_TO_INT = {
    "success": LogStatusInt.SUCCESS,
    "ok": LogStatusInt.SUCCESS,
    "failure": LogStatusInt.FAILURE,
    "error": LogStatusInt.FAILURE,
    "exception": LogStatusInt.FAILURE,
    "timeout": LogStatusInt.TIMEOUT,
    "skipped": LogStatusInt.SKIPPED
}

STATUS_INT_TO_STR = {
    LogStatusInt.SUCCESS: "success",
    LogStatusInt.FAILURE: "failure",
    LogStatusInt.TIMEOUT: "timeout",
    LogStatusInt.SKIPPED: "skipped"
}

def generate_trace_id() -> str:
    """Generates a 32-hex-character W3C-compliant trace ID."""
    return uuid.uuid4().hex

def generate_span_id() -> str:
    """Generates a 16-hex-character W3C-compliant span ID."""
    return uuid.uuid4().hex[:16]

def trace_id_to_bytes(trace_id_str: str) -> bytes:
    """Converts a 32-char hex string or UUID into 16 raw binary bytes."""
    clean = trace_id_str.replace("-", "").strip()
    try:
        if len(clean) == 32:
            return bytes.fromhex(clean)
        return uuid.UUID(trace_id_str).bytes
    except Exception:
        return clean.encode("utf-8")[:16].ljust(16, b"\x00")

def bytes_to_trace_id(b: Union[bytes, memoryview, str]) -> str:
    """Converts 16 raw binary bytes back to a 32-char hex trace ID string."""
    if isinstance(b, str):
        return b
    if isinstance(b, memoryview):
        b = b.tobytes()
    return b.hex()

def span_id_to_bytes(span_id_str: str) -> bytes:
    """Converts a 16-char hex string into 8 raw binary bytes."""
    clean = span_id_str.replace("-", "").strip()[:16]
    try:
        return bytes.fromhex(clean.ljust(16, "0"))
    except Exception:
        return clean.encode("utf-8")[:8].ljust(8, b"\x00")

def bytes_to_span_id(b: Union[bytes, memoryview, str]) -> str:
    """Converts 8 raw binary bytes back to a 16-char hex span ID string."""
    if isinstance(b, str):
        return b
    if isinstance(b, memoryview):
        b = b.tobytes()
    return b.hex()

def current_unix_microseconds() -> int:
    """Returns integer Unix timestamp in microseconds (8 bytes in SQLite)."""
    return int(time.time() * 1_000_000)

def current_microsecond_iso() -> str:
    """Returns ISO 8601 timestamp with microsecond precision in UTC."""
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def microseconds_to_iso(ts_micros: int) -> str:
    """Converts microsecond integer epoch into ISO 8601 UTC string."""
    seconds = ts_micros / 1_000_000.0
    dt = datetime.datetime.fromtimestamp(seconds, tz=datetime.timezone.utc)
    return dt.isoformat()

@dataclass
class LogEvent:
    """
    Standardized production-grade log record.
    Guaranteed machine-readable shape across all services and modules.
    """
    timestamp: str = field(default_factory=current_microsecond_iso)
    epoch_ns: int = field(default_factory=time.time_ns)
    ts_micros: int = field(default_factory=current_unix_microseconds)
    level: LogLevel = LogLevel.INFO
    level_int: LogLevelInt = LogLevelInt.INFO
    service: str = "alips-stream-engine"
    module: str = "core"
    function: str = "unknown"
    line_no: int = 0
    trace_id: str = field(default_factory=generate_trace_id)
    span_id: str = field(default_factory=generate_span_id)
    parent_span_id: Optional[str] = None
    event: str = "system_event"
    duration_ms: float = 0.0
    status: str = "success"
    status_int: LogStatusInt = LogStatusInt.SUCCESS
    payload: Dict[str, Any] = field(default_factory=dict)
    environment: str = "production"

    def __post_init__(self):
        if isinstance(self.level, str):
            lvl_upper = self.level.upper()
            self.level_int = LEVEL_STR_TO_INT.get(lvl_upper, LogLevelInt.INFO)
        if isinstance(self.status, str):
            self.status_int = STATUS_STR_TO_INT.get(self.status.lower(), LogStatusInt.SUCCESS)

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        if isinstance(self.level, (LogLevel, LogLevelInt)):
            d["level"] = self.level.value if hasattr(self.level, "value") else str(self.level)
        return d

@dataclass
class MetricEvent:
    timestamp: str = field(default_factory=current_microsecond_iso)
    name: str = "metric.default"
    metric_type: str = "gauge" # counter, gauge, histogram
    value: float = 0.0
    unit: str = "ms"
    labels: Dict[str, str] = field(default_factory=dict)
    service: str = "alips-stream-engine"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

@dataclass
class SpanEvent:
    trace_id: str
    span_id: str
    parent_span_id: Optional[str]
    name: str
    service: str
    start_time_iso: str
    end_time_iso: str
    duration_ms: float
    status: str = "OK"
    attributes: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
