"""
CLI Utility to Inspect the Zero-Deletion Telemetry Archive.
Run:
    python3 observability/viewer.py stats
    python3 observability/viewer.py logs --limit 20
    python3 observability/viewer.py trace <trace_id>
"""
import sys
import os
import json
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from observability.storage import TelemetryStorageEngine

def main():
    parser = argparse.ArgumentParser(description="ALIPS Zero-Deletion Telemetry Inspector")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("stats", help="Show archive storage statistics and compression efficiency")

    logs_parser = subparsers.add_parser("logs", help="Query recent logs")
    logs_parser.add_argument("--level", type=str, default=None)
    logs_parser.add_argument("--service", type=str, default=None)
    logs_parser.add_argument("--trace", type=str, default=None)
    logs_parser.add_argument("--limit", type=int, default=20)

    trace_parser = subparsers.add_parser("trace", help="View full distributed trace waterfall")
    trace_parser.add_argument("trace_id", type=str)

    args = parser.parse_args()
    storage = TelemetryStorageEngine()

    if args.command == "stats" or not args.command:
        stats = storage.get_storage_stats()
        print("\n" + "=" * 70)
        print("📊 ALIPS OBSERVABILITY ARCHIVE HEALTH & CAPACITY REPORT")
        print("=" * 70)
        print(f"📁 Database Path:           {stats['db_path']}")
        print(f"📦 Compression Engine:      {stats['compression_engine']}")
        print(f"📜 Total Log Records:       {stats['log_count']:,}")
        print(f"📈 Total Metric Points:     {stats['metric_count']:,}")
        print(f"⚡ Total Spans Recorded:    {stats['span_count']:,}")
        print(f"💾 Total Disk Footprint:    {stats['total_disk_mb']} MB ({stats['total_disk_bytes']:,} bytes)")
        if stats['log_count'] > 0:
            ratio = round((stats['estimated_uncompressed_mb'] / max(stats['total_disk_mb'], 0.001)), 1)
            print(f"📉 Estimated Raw Size:      {stats['estimated_uncompressed_mb']} MB (Compression: ~{ratio}x reduction)")
        print("=" * 70 + "\n")

    elif args.command == "logs":
        logs = storage.query_logs(
            level=args.level,
            service=args.service,
            trace_id=args.trace,
            limit=args.limit
        )
        print(f"\nFound {len(logs)} logs:")
        for l in reversed(logs):
            print(f"[{l['timestamp']}] [{l['level']:<5}] [{l['service']}:{l['function']}] {l['event']} ({l['duration_ms']:.2f}ms) [trace={l['trace_id'][:8]}..]")
            if l['payload']:
                print(f"   Payload: {json.dumps(l['payload'], default=str)}")

    elif args.command == "trace":
        trace_data = storage.query_trace(args.trace_id)
        print(f"\nTrace Waterfall for {args.trace_id}:")
        print(f"Spans ({len(trace_data['spans'])}):")
        for s in trace_data['spans']:
            print(f"  └── [{s['service']}] {s['name']} -> {s['duration_ms']:.2f}ms (Status: {s['status']})")
        print(f"Associated Logs ({len(trace_data['logs'])}):")
        for l in trace_data['logs']:
            print(f"      [{l['level']}] {l['event']} ({l['function']})")

if __name__ == "__main__":
    main()
