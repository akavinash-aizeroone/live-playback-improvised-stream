"""
Observability Package.
OpenTelemetry-standard structured logs, metrics, distributed traces, and zero-deletion SQLite archive.
"""
from observability.schema import LogLevel, LogEvent, MetricEvent, SpanEvent
from observability.sanitizer import sanitize_payload
from observability.storage import TelemetryStorageEngine
from observability.logger import (
    TelemetryLogger, LOGGER, get_logger, logged, trace_span,
    get_current_trace_id, set_current_trace_id
)

__all__ = [
    "LogLevel",
    "LogEvent",
    "MetricEvent",
    "SpanEvent",
    "sanitize_payload",
    "TelemetryStorageEngine",
    "TelemetryLogger",
    "LOGGER",
    "get_logger",
    "logged",
    "trace_span",
    "get_current_trace_id",
    "set_current_trace_id"
]
