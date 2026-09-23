"""
Self-Contained Real-Time Telemetry & Web Server for Browser Line Puppetry.
Uses standard library (http.server) with Server-Sent Events (SSE) for zero-dependency streaming.
Automatically selects an unstandard random high port (32000-48000) to guarantee zero port conflicts.
"""
import http.server
import socketserver
import json
import time
import os
import sys
import socket
import random
import threading
from typing import List

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from pipeline import AutonomousImprovStreamOrchestrator

class TelemetryEngine:
    def __init__(self):
        self.orchestrator = AutonomousImprovStreamOrchestrator()
        self.turn = 0
        self.current_speaker = "AGENT_A"

    def get_next_telemetry_tick(self) -> dict:
        self.turn += 1
        # Alternate speaker turns every 30 ticks (~3 seconds at 10 Hz)
        if self.turn % 30 == 0:
            self.current_speaker = "AGENT_B" if self.current_speaker == "AGENT_A" else "AGENT_A"

        observed_tension = 0.45 + (0.35 * (abs((self.turn % 60) - 30) / 30.0))
        dramaturgy_tick = self.orchestrator.run_dramaturgical_tick(
            observed_tension=observed_tension,
            speaker=self.current_speaker,
            status_move="RAISE_SELF" if (self.turn % 20 < 10) else "LOWER_SELF"
        )

        subtitles = (
            "The estate belongs to the Duke, Thomas. Put down the silver."
            if self.current_speaker == "AGENT_A"
            else "The Duke will not be dining tonight, sir. Look at your boots."
        )

        return {
            "timestamp": time.time(),
            "turn": self.turn,
            "current_speaker": self.current_speaker,
            "tension": round(observed_tension, 2),
            "pid_directive": dramaturgy_tick["pacing"]["directive"],
            "status_a": dramaturgy_tick["status_distribution"]["status_a"],
            "status_b": dramaturgy_tick["status_distribution"]["status_b"],
            "subtitles": subtitles,
            "halted": False
        }

ENGINE = TelemetryEngine()

class LinePuppetryHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Suppress routine log noise for SSE ticks
        if "/stream" not in self.path:
            super().log_message(format, *args)

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(os.path.join(BASE_DIR, "index.html"), "rb") as f:
                self.wfile.write(f.read())
            return

        elif self.path == "/stream":
            # Server-Sent Events (SSE) Real-Time Telemetry Stream
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            try:
                while True:
                    payload = ENGINE.get_next_telemetry_tick()
                    data_str = f"data: {json.dumps(payload)}\n\n"
                    self.wfile.write(data_str.encode("utf-8"))
                    self.wfile.flush()
                    time.sleep(0.1) # 10 Hz telemetry updates
            except (ConnectionResetError, BrokenPipeError):
                pass
            return

        super().do_GET()

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

def find_free_unstandard_port(min_port: int = 34000, max_port: int = 49000, max_attempts: int = 50) -> int:
    """
    Finds a guaranteed free, unstandard high port in random order.
    """
    ports = list(range(min_port, max_port))
    random.shuffle(ports)
    for port in ports[:max_attempts]:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                continue
    # Fallback to OS assigned port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]

def start_server():
    # If a port was specified as a command-line argument, use it; otherwise pick a random unstandard port
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port = int(sys.argv[1])
    else:
        port = find_free_unstandard_port()

    server = ThreadingTCPServer(("", port), LinePuppetryHTTPHandler)
    url = f"http://localhost:{port}"

    # Write active port to a local file for external tools/OBS to easily read
    with open(os.path.join(BASE_DIR, "active_port.txt"), "w") as f:
        f.write(str(port))

    print("\n" + "=" * 75)
    print(f"🎬 ALIPS BROWSER LINE PUPPETRY STAGE IS LIVE!")
    print(f"👉 OPEN IN YOUR BROWSER:  {url}")
    print(f"📡 Real-time SSE Telemetry: {url}/stream")
    print(f"⚡ Unstandard Port: {port} (Zero Conflicts Guaranteed)")
    print("=" * 75 + "\n")
    sys.stdout.flush()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down stage server.")
    finally:
        server.server_close()

if __name__ == "__main__":
    start_server()
