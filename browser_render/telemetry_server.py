"""
WebSocket Telemetry Server for Browser-Native Line Puppetry.
Bridges ALIPS Dramaturgy, Perception, and Safety to the HTML5 Canvas client.
Streams status distribution, dramatic tension, subtitles, and forum intervention flags.
"""
import asyncio
import json
import time
from typing import Set
import websockets

from pipeline import AutonomousImprovStreamOrchestrator

CONNECTED_CLIENTS: Set[websockets.WebSocketServerProtocol] = set()

class BrowserTelemetryServer:
    def __init__(self, host: str = "0.0.0.0", port: int = 8765):
        self.host = host
        self.port = port
        self.orchestrator = AutonomousImprovStreamOrchestrator()
        self.running = True
        self.current_speaker = "AGENT_A"

    async def register(self, websocket: websockets.WebSocketServerProtocol):
        CONNECTED_CLIENTS.add(websocket)
        print(f"[WS] Client connected. Total active clients: {len(CONNECTED_CLIENTS)}")
        try:
            await websocket.wait_closed()
        finally:
            CONNECTED_CLIENTS.remove(websocket)
            print(f"[WS] Client disconnected. Active clients: {len(CONNECTED_CLIENTS)}")

    async def broadcast(self, payload: dict):
        if not CONNECTED_CLIENTS:
            return
        message = json.dumps(payload)
        await asyncio.gather(
            *[client.send(message) for client in CONNECTED_CLIENTS],
            return_exceptions=True
        )

    async def telemetry_loop(self):
        """
        Emits 20 Hz / 60 Hz telemetry state to connected browser renderers.
        """
        turn = 0
        while self.running:
            turn += 1
            # Alternate speaker turns every 8 seconds
            if turn % 40 == 0:
                self.current_speaker = "AGENT_B" if self.current_speaker == "AGENT_A" else "AGENT_A"

            # Execute a tick on the ALIPS dramaturgy engine
            observed_tension = 0.45 + (0.35 * (abs((turn % 60) - 30) / 30.0))
            dramaturgy_tick = self.orchestrator.run_dramaturgical_tick(
                observed_tension=observed_tension,
                speaker=self.current_speaker,
                status_move="RAISE_SELF" if (turn % 20 < 10) else "LOWER_SELF"
            )

            # Build telemetry payload
            payload = {
                "timestamp": time.time(),
                "turn": turn,
                "current_speaker": self.current_speaker,
                "tension": round(observed_tension, 2),
                "pid_directive": dramaturgy_tick["pacing"]["directive"],
                "status_a": dramaturgy_tick["status_distribution"]["status_a"],
                "status_b": dramaturgy_tick["status_distribution"]["status_b"],
                "subtitles": (
                    "The estate belongs to the Duke, Thomas. Put down the silver."
                    if self.current_speaker == "AGENT_A"
                    else "The Duke will not be dining tonight, sir. Look at your boots."
                ),
                "halted": False
            }

            await self.broadcast(payload)
            await asyncio.sleep(0.05) # 20 updates/sec (browser smoothly lerps at 60/120 FPS)

    async def run(self):
        print(f"🚀 ALIPS Browser Telemetry Server listening on ws://{self.host}:{self.port}")
        server = await websockets.serve(self.register, self.host, self.port)
        await asyncio.gather(server.wait_closed(), self.telemetry_loop())

if __name__ == "__main__":
    server = BrowserTelemetryServer()
    try:
        asyncio.run(server.run())
    except KeyboardInterrupt:
        print("\nTelemetry server shut down.")
