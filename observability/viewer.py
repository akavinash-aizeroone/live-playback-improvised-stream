"""
CLI Utility to Inspect and Maintain the Zero-Deletion Telemetry Archive.
Run:
    python3 observability/viewer.py stats
    python3 observability/viewer.py logs --limit 20
    python3 observability/viewer.py trace <trace_id>
    python3 observability/viewer.py recompress --days 30 --level 19
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
    logs_parser.add_argument("--event", type=str, default=None)
    logs_parser.add_argument("--limit", type=int, default=20)

    trace_parser = subparsers.add_parser("trace", help="View full distributed trace waterfall")
    trace_parser.add_argument("trace_id", type=str)

    recomp_parser = subparsers.add_parser("recompress", help="Execute offline cold archival recompression")
    recomp_parser.add_argument("--days", type=int, default=30)
    recomp_parser.add_argument("--level", type=int, default=19)

    args = parser.parse_args()
    storage = TelemetryStorageEngine()

    if args.command == "stats" or not args.command:
        stats = storage.get_storage_stats()
        print("\n" + "=" * 75)
        print("📊 ALIPS OBSERVABILITY ARCHIVE HEALTH & CAPACITY REPORT")
        print("=" * 75)
        print(f"📁 Database Path:               {stats['db_path']}")
        print(f"📦 Compression Engine:          {stats['compression_engine']}")
        print(f"📜 Total Log Records:           {stats['log_count']:,}")
        print(f"🏷️ Unique Services:             {stats.get('unique_services', 0)}")
        print(f"⚡ Unique Event Codes:          {stats.get('unique_events', 0)}")
        print(f"📈 Total Metric Points:         {stats['metric_count']:,}")
        print(f"🌲 Total Spans Recorded:        {stats['span_count']:,}")
        print(f"💾 Total Disk Footprint:        {stats['total_disk_mb']} MB ({stats['total_disk_bytes']:,} bytes)")
        print(f"🛡️ 5-Year Storage Projection:   ~{stats.get('estimated_5_year_footprint_mb', 16.0)} MB (Zero-Deletion Budget: 20MB)")
        print("=" * 75 + "\n")

    elif args.command == "logs":
        logs = storage.query_logs(
            level=args.level,
            service=args.service,
            trace_id=args.trace,
            event=args.event,
            limit=args.limit
        )
        print(f"\nFound {len(logs)} logs:")
        for l in reversed(logs):
            print(f"[{l['timestamp']}] [{l['level']:<5}] [{l['service']}:{l['event']}] status={l['status']} ({l['duration_ms']}ms) [trace={l['trace_id'][:8]}..]")
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
            print(f"      [{l['level']}] {l['event']} (status={l['status']})")

    elif args.command == "recompress":
        res = storage.recompress_cold_logs(age_days=args.days, target_level=args.level)
        print(f"\nRecompression Complete:")
        print(f"  Records Recompressed: {res.get('recompressed_records', 0)}")
        print(f"  Bytes Saved:          {res.get('bytes_saved', 0)}")
        print(f"  Cutoff Age:           {res.get('cutoff_age_days', 30)} days")
        print(f"  Target Zstd Level:    {res.get('target_zstd_level', 19)}")

if __name__ == "__main__":
    main()
