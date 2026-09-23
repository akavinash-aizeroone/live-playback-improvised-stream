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
                    "dialogue": f"Hold on a second. Did you just say '{clean_word}'?! Vincent, look at me. Did this boy just bring up '{clean_word}'?!",
                    "statusA": 9.4,
                    "statusB": 2.0,
                    "tension": 0.88,
                    "targetA": 0.52,
                    "targetB": 0.70,
                    "gestureA": "DRAW_PISTOL",
                    "gestureB": "FLINCH_TERROR",
                    "camZoom": 1.7,
                    "camLabel": "IMPROV TILT: " + clean_word[:14].upper(),
                    "shake": 0.5,
                    "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": f"Jules, I swear on my life! Marcellus Wallace told us the '{clean_word}' was already taken care of in the cupboard!",
                    "statusA": 9.2,
                    "statusB": 3.8,
                    "tension": 0.94,
                    "targetA": 0.54,
                    "targetB": 0.70,
                    "gestureA": "ROAR_AIM",
                    "gestureB": "PLEADING_TERROR",
                    "camZoom": 1.9,
                    "camLabel": "SPECT-ACTOR REACTION",
                    "shake": 0.7,
                    "improvised": True
                },
                {
                    "id": current_beat_id + 3,
                    "speaker": "A",
                    "dialogue": f"Well then today is your reckoning day with '{clean_word}'! Because the Lord does not negotiate over '{clean_word}'!",
                    "statusA": 10.0,
                    "statusB": 1.0,
                    "tension": 1.0,
                    "targetA": 0.58,
                    "targetB": 0.70,
                    "gestureA": "ROAR_EZEKIEL_CLIMAX",
                    "gestureB": "FLINCH_TERROR",
                    "camZoom": 2.1,
                    "camLabel": "IMPROVISED CLIMAX",
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
                    "dialogue": f"Good heavens! What on earth does '{clean_word}' have to do with the Grand Duke's affairs?!",
                    "statusA": 6.5,
                    "statusB": 6.0,
                    "tension": 0.82,
                    "targetA": 0.42,
                    "targetB": 0.65,
                    "gestureA": "SHOCK",
                    "gestureB": "STAND_TALL",
                    "camZoom": 1.4,
                    "camLabel": "IMPROV TILT: " + clean_word[:14].upper(),
                    "shake": 0.4,
                    "improvised": True
                },
                {
                    "id": current_beat_id + 2,
                    "speaker": "B",
                    "dialogue": f"Everything, sir! The '{clean_word}' was found locked under the floorboards in the master suite!",
                    "statusA": 3.0,
                    "statusB": 9.0,
                    "tension": 0.95,
                    "targetA": 0.45,
                    "targetB": 0.60,
                    "gestureA": "FALL_KNEE",
                    "gestureB": "TRIUMPH",
                    "camZoom": 1.7,
                    "camLabel": "SPECT-ACTOR REVERSAL",
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
        if self.path == "/api/improvise":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"
            try:
                data = json.loads(body)
            except Exception:
                data = {}

            prompt_words = data.get("prompt_words", "").strip()
            scene_key = data.get("scene", "pulp_fiction")
            intensity = data.get("intensity", "tilt")
            current_beat_id = int(data.get("current_beat_id", 1))

            new_beats = AppliedAIImprovGenerator.generate(
                scene_key=scene_key,
                user_word=prompt_words,
                intensity=intensity,
                current_beat_id=current_beat_id
            )

            response = {
                "success": True,
                "prompt_words": prompt_words,
                "scene": scene_key,
                "improvised_beats": new_beats
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
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(os.path.join(BASE_DIR, "index.html"), "rb") as f:
                self.wfile.write(f.read())
            return

        elif self.path == "/stream":
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
