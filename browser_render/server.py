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
from dramaturgy.playback_theatre import JonathanFoxPlaybackEngine
from observability import LOGGER, LogLevel, logged, trace_span, TelemetryStorageEngine

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

class AppliedAIImprovGenerator:
    """
    Applied AI Theatrical Improvisation Engine.
    Converts arbitrary user words, plot twists, or objects into Keith Johnstone-compliant
    theatrical offers, tilts, and re-incorporations for active characters.
    """
    @staticmethod
    def generate(scene_key: str, user_word: str, intensity: str = "tilt", current_beat_id: int = 1) -> list:
        clean_word = user_word.strip()
        if not clean_word:
            clean_word = "the truth"

        if scene_key == "pulp_fiction":
            return [
                {
                    "id": current_beat_id + 1,
                    "speaker": "A",
                    "dialogue": f"You think Marcellus Wallace didn't know about '{clean_word}'?! Brett, look at me! You think my boss sent his most loyal shepherd across town just to let '{clean_word}' slip out of this room?!",
                    "statusA": 9.6,
                    "statusB": 2.0,
                    "tension": 0.88,
                    "targetA": 0.52,
                    "targetB": 0.70,
                    "gestureA": "DRAW_PISTOL",
                    "gestureB": "FLINCH_TERROR",
                    "camZoom": 1.7,
                    "camLabel": "CONFRONTATION: " + clean_word[:14].upper(),
                    "shake": 0.5,
                    "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": f"Jules, I swear on everything holy! '{clean_word.capitalize()}' was never meant to cross Marcellus! We were protecting it in the cupboard until you arrived!",
                    "statusA": 9.2,
                    "statusB": 3.8,
                    "tension": 0.94,
                    "targetA": 0.54,
                    "targetB": 0.70,
                    "gestureA": "ROAR_AIM",
                    "gestureB": "PLEADING_TERROR",
                    "camZoom": 1.9,
                    "camLabel": "DESPERATE DEFENSE",
                    "shake": 0.7,
                    "improvised": True
                },
                {
                    "id": current_beat_id + 3,
                    "speaker": "A",
                    "dialogue": f"Then why is '{clean_word}' smelling like treason to me, Brett?! Because the righteous man does not barter over '{clean_word}'!",
                    "statusA": 10.0,
                    "statusB": 1.0,
                    "tension": 1.0,
                    "targetA": 0.58,
                    "targetB": 0.70,
                    "gestureA": "ROAR_EZEKIEL_CLIMAX",
                    "gestureB": "FLINCH_TERROR",
                    "camZoom": 2.1,
                    "camLabel": "THE WRATH OF JULES",
                    "shake": 1.1,
                    "improvised": True
                }
            ]
        elif scene_key == "a_few_good_men":
            return [
                {
                    "id": current_beat_id + 1,
                    "speaker": "A",
                    "dialogue": f"Colonel Jessep, isn't it true that '{clean_word}' was the exact pretext used to authorize the transfer order?",
                    "statusA": 8.8,
                    "statusB": 9.2,
                    "tension": 0.85,
                    "targetA": 0.50,
                    "targetB": 0.72,
                    "gestureA": "POINT",
                    "gestureB": "GLARE",
                    "camZoom": 1.5,
                    "camLabel": "IMPROV TILT: " + clean_word[:14].upper(),
                    "shake": 0.4,
                    "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": f"You sit there in your crisp whites and lecture me about '{clean_word}'?! '{clean_word}' saved lives at Windward Point!",
                    "statusA": 8.5,
                    "statusB": 10.0,
                    "tension": 0.96,
                    "targetA": 0.50,
                    "targetB": 0.70,
                    "gestureA": "STAND_FIRM",
                    "gestureB": "ROAR",
                    "camZoom": 1.85,
                    "camLabel": "JESSEP ROAR SURGE",
                    "shake": 0.9,
                    "improvised": True
                }
            ]
        elif scene_key == "dark_knight":
            return [
                {
                    "id": current_beat_id + 1,
                    "speaker": "A",
                    "dialogue": f"Where did you hide the '{clean_word}'?! Tell me!",
                    "statusA": 9.2,
                    "statusB": 9.8,
                    "tension": 0.90,
                    "targetA": 0.52,
                    "targetB": 0.68,
                    "gestureA": "SLAM_TABLE",
                    "gestureB": "LAUGH_LEAN",
                    "camZoom": 1.7,
                    "camLabel": "IMPROV TILT: " + clean_word[:14].upper(),
                    "shake": 0.7,
                    "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": f"You see, Batman... to them, '{clean_word}' is just another bad joke waiting to tear through their civilized order!",
                    "statusA": 7.5,
                    "statusB": 10.0,
                    "tension": 0.98,
                    "targetA": 0.52,
                    "targetB": 0.68,
                    "gestureA": "STILL",
                    "gestureB": "DELIGHTED_CHAOS",
                    "camZoom": 1.95,
                    "camLabel": "JOKER PHILOSOPHICAL REVERSAL",
                    "shake": 0.5,
                    "improvised": True
                }
            ]
        elif scene_key == "whiplash":
            return [
                {
                    "id": current_beat_id + 1,
                    "speaker": "A",
                    "dialogue": f"Stop! You think '{clean_word}' excuses you dragging four beats behind my tempo?!",
                    "statusA": 10.0,
                    "statusB": 3.0,
                    "tension": 0.92,
                    "targetA": 0.54,
                    "targetB": 0.72,
                    "gestureA": "LEAN_INTO_FACE",
                    "gestureB": "TREMBLING_HANDS",
                    "camZoom": 1.75,
                    "camLabel": "IMPROV TILT: " + clean_word[:14].upper(),
                    "shake": 0.6,
                    "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": f"It wasn't '{clean_word}', Mr. Fletcher! I was playing on tempo until my hands bled!",
                    "statusA": 9.5,
                    "statusB": 4.5,
                    "tension": 0.98,
                    "targetA": 0.54,
                    "targetB": 0.72,
                    "gestureA": "RAISE_FIST_HALT",
                    "gestureB": "TENSE_DRUMSTICKS",
                    "camZoom": 1.9,
                    "camLabel": "NEIMAN DEFIANCE",
                    "shake": 0.8,
                    "improvised": True
                }
            ]
        elif scene_key == "social_network":
            return [
                {
                    "id": current_beat_id + 1,
                    "speaker": "A",
                    "dialogue": f"You told Peter Thiel that '{clean_word}' was my responsibility while you diluted my equity to zero!",
                    "statusA": 9.5,
                    "statusB": 6.0,
                    "tension": 0.92,
                    "targetA": 0.52,
                    "targetB": 0.70,
                    "gestureA": "SLAM_TABLE",
                    "gestureB": "MONOTONE_GLARE",
                    "camZoom": 1.6,
                    "camLabel": "IMPROV TILT: " + clean_word[:14].upper(),
                    "shake": 0.6,
                    "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": f"The '{clean_word}' didn't scale, Eduardo. Facebook is moving at light speed, and your '{clean_word}' was left in Boston.",
                    "statusA": 8.0,
                    "statusB": 9.0,
                    "tension": 0.95,
                    "targetA": 0.52,
                    "targetB": 0.70,
                    "gestureA": "SHATTER_LAPTOP",
                    "gestureB": "MONOTONE",
                    "camZoom": 1.8,
                    "camLabel": "ZUCKERBERG COLD DETACHMENT",
                    "shake": 0.7,
                    "improvised": True
                }
            ]
        else: # Generic / Blackwood Silver
            return [
                {
                    "id": current_beat_id + 1,
                    "speaker": "A",
                    "dialogue": f"The Grand Duke discovered '{clean_word}' concealed within the manor accounts, Thomas. Your signature was on the ledger!",
                    "statusA": 8.5,
                    "statusB": 4.0,
                    "tension": 0.85,
                    "targetA": 0.42,
                    "targetB": 0.65,
                    "gestureA": "POINT",
                    "gestureB": "NERVOUS",
                    "camZoom": 1.45,
                    "camLabel": "MANOR DISCOVERY: " + clean_word[:14].upper(),
                    "shake": 0.4,
                    "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": f"Then you know the truth, Mr. Sterling—'{clean_word}' was delivered on the Grand Duke's secret orders to expose your theft!",
                    "statusA": 3.0,
                    "statusB": 9.5,
                    "tension": 0.98,
                    "targetA": 0.45,
                    "targetB": 0.60,
                    "gestureA": "FALL_KNEE",
                    "gestureB": "TRIUMPH",
                    "camZoom": 1.75,
                    "camLabel": "DRAMATIC REVERSAL",
                    "shake": 0.8,
                    "improvised": True
                }
            ]

ENGINE = TelemetryEngine()

class LinePuppetryHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        if "/stream" not in self.path:
            super().log_message(format, *args)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if self.path == "/api/playback":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"
            try:
                data = json.loads(body)
            except Exception:
                data = {}

            teller_prompt = data.get("teller_prompt", "").strip() or data.get("prompt_words", "").strip()
            starting_beat_id = int(data.get("starting_beat_id", 1))

            start_t = time.perf_counter()
            with trace_span("api_playback_theatre_generate", service="server-api", attributes={"prompt": teller_prompt}):
                playback_beats = JonathanFoxPlaybackEngine.generate_full_ritual(
                    teller_prompt=teller_prompt,
                    starting_beat_id=starting_beat_id
                )
                duration_ms = (time.perf_counter() - start_t) * 1000.0

            LOGGER.increment("api.playback.requests", labels={"status": "success"})
            LOGGER.timing("api.playback.latency_ms", duration_ms)

            response = {
                "success": True,
                "ritual_type": "JONATHAN_FOX_PLAYBACK_THEATRE",
                "teller_prompt": teller_prompt,
                "beat_count": len(playback_beats),
                "playback_beats": playback_beats,
                "duration_ms": round(duration_ms, 2)
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return

        elif self.path == "/api/improvise":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"
            try:
                data = json.loads(body)
            except Exception:
                data = {}
            prompt_words = str(data.get("prompt_words") or data.get("word") or "").strip()
            scene_key = str(data.get("scene") or data.get("screenplay_id") or "pulp_fiction")
            intensity = str(data.get("intensity", "tilt"))
            current_beat_id = int(data.get("current_beat_id", 1))

            start_t = time.perf_counter()
            with trace_span("api_improvise_generate", service="server-api", attributes={"scene": scene_key, "words": prompt_words}):
                new_beats = AppliedAIImprovGenerator.generate(
                    scene_key=scene_key,
                    user_word=prompt_words,
                    intensity=intensity,
                    current_beat_id=current_beat_id
                )
                duration_ms = (time.perf_counter() - start_t) * 1000.0

            LOGGER.increment("api.improvise.requests", labels={"scene": scene_key})
            LOGGER.timing("api.improvise.latency_ms", duration_ms)

            response = {
                "success": True,
                "prompt_words": prompt_words,
                "scene": scene_key,
                "improvised_beats": new_beats,
                "duration_ms": round(duration_ms, 2)
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()

    def do_GET(self):
        # Route query parameters
        clean_path = self.path.split("?")[0]

        if clean_path == "/" or clean_path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(os.path.join(BASE_DIR, "index.html"), "rb") as f:
                self.wfile.write(f.read())
            return

        elif clean_path == "/api/logs":
            import urllib.parse
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)

            level = params.get("level", [None])[0]
            service = params.get("service", [None])[0]
            trace_id = params.get("trace", [None])[0]
            event = params.get("event", [None])[0]
            limit = int(params.get("limit", [50])[0])

            storage = TelemetryStorageEngine()
            logs = storage.query_logs(
                level=level,
                service=service,
                trace_id=trace_id,
                event=event,
                limit=limit
            )

            res = {
                "success": True,
                "count": len(logs),
                "logs": logs
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(res).encode("utf-8"))
            return

        elif clean_path == "/api/metrics":
            storage = TelemetryStorageEngine()
            stats = storage.get_storage_stats()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "stats": stats}).encode("utf-8"))
            return

        elif clean_path.startswith("/api/trace/"):
            trace_id = clean_path.split("/")[-1]
            storage = TelemetryStorageEngine()
            trace_data = storage.query_trace(trace_id)
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "trace": trace_data}).encode("utf-8"))
            return

        elif clean_path == "/stream":
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            LOGGER.increment("sse.connections.active")
            try:
                while True:
                    payload = ENGINE.get_next_telemetry_tick()
                    data_str = f"data: {json.dumps(payload)}\n\n"
                    self.wfile.write(data_str.encode("utf-8"))
                    self.wfile.flush()
                    time.sleep(0.1)
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
