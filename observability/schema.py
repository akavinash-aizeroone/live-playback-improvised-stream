"""
OpenTelemetry-Compatible Structured Telemetry Schema.
Standardized across logs, metrics, and distributed traces.
Adheres to W3C Trace Context and CloudEvents specifications.
"""
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Dict, Any, Optional
import datetime
import uuid
import time

class LogLevel(str, Enum):
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

def generate_trace_id() -> str:
    """Generates a 32-hex-character W3C-compliant trace ID."""
    return uuid.uuid4().hex

def generate_span_id() -> str:
    """Generates a 16-hex-character W3C-compliant span ID."""
    return uuid.uuid4().hex[:16]

def current_microsecond_iso() -> str:
    """Returns ISO 8601 timestamp with microsecond precision in UTC."""
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

@dataclass
class LogEvent:
    """
    Standardized production-grade log record.
    Guaranteed machine-readable shape across all services and modules.
    """
    timestamp: str = field(default_factory=current_microsecond_iso)
    epoch_ns: int = field(default_factory=time.time_ns)
    level: LogLevel = LogLevel.INFO
    service: str = "alips-stream-engine"
    module: str = "core"
    function: str = "unknown"
    line_no: int = 0
    trace_id: str = field(default_factory=generate_trace_id)
    span_id: str = field(default_factory=generate_span_id)
    parent_span_id: Optional[str] = None
    event: str = "system_event"
    duration_ms: float = 0.0
    payload: Dict[str, Any] = field(default_factory=dict)
    environment: str = "production"

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        if isinstance(self.level, LogLevel):
            d["level"] = self.level.value
        return d

@dataclass
class MetricEvent:
    """
    Standardized metric record for telemetry aggregation (Counters, Gauges, Histograms).
    """
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
    """
    Standardized distributed tracing span record for end-to-end latency waterfall graphs.
    """
    trace_id: str
    span_id: str
    parent_span_id: Optional[str]
    name: str
    service: str
    start_time_iso: str
    end_time_iso: str
    duration_ms: float
    status: str = "OK" # OK, ERROR
    attributes: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
