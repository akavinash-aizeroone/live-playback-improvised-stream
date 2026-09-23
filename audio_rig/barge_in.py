"""
Audio Rigging & Low-Latency Barge-In Interruption Controller.
Handles anti-pop Hann window crossfades, Unreal Live Link Face UDP packets,
and VTube Studio Live2D WebSocket parameters.
"""
import struct
import time
import numpy as np
from typing import Dict, Any

# Canonical 52 ARKit Blendshape Names
ARKIT_BLENDSHAPES = [
    "EyeBlinkLeft", "EyeLookDownLeft", "EyeLookInLeft", "EyeLookOutLeft", "EyeLookUpLeft",
    "EyeSquintLeft", "EyeWideLeft", "EyeBlinkRight", "EyeLookDownRight", "EyeLookInRight",
    "EyeLookOutRight", "EyeLookUpRight", "EyeSquintRight", "EyeWideRight", "JawForward",
    "JawLeft", "JawRight", "JawOpen", "MouthClose", "MouthFunnel", "MouthPucker",
    "MouthLeft", "MouthRight", "MouthSmileLeft", "MouthSmileRight", "MouthFrownLeft",
    "MouthFrownRight", "MouthDimpleLeft", "MouthDimpleRight", "MouthStretchLeft",
    "MouthStretchRight", "MouthRollLower", "MouthRollUpper", "MouthShrugLower",
    "MouthShrugUpper", "MouthPressLeft", "MouthPressRight", "MouthLowerDownLeft",
    "MouthLowerDownRight", "MouthUpperUpLeft", "MouthUpperUpRight", "BrowDownLeft",
    "BrowDownRight", "BrowInnerUp", "BrowOuterUpLeft", "BrowOuterUpRight", "CheekPuff",
    "CheekSquintLeft", "CheekSquintRight", "NoseSneerLeft", "NoseSneerRight", "TongueOut"
]

class AudioBargeInController:
    """
    Manages audio streaming buffers and ensures seamless barge-in interruption
    by applying a smooth 12-15ms Hann window decay before buffer wipe.
    Prevents speaker driver DC pop/clicks.
    """
    def __init__(self, sample_rate: int = 24000, fade_ms: float = 15.0):
        self.sample_rate = sample_rate
        self.fade_ms = fade_ms
        self.fade_samples = int(sample_rate * (fade_ms / 1000.0))
        self.buffer = bytearray()
        self.is_playing = False

    def push_pcm_chunk(self, chunk: bytes):
        self.buffer.extend(chunk)
        self.is_playing = True

    def execute_barge_in_cut(self) -> bytes:
        """
        Executes an emergency interruption:
        Takes the trailing slice of audio, applies a cosine Hann ramp to zero,
        flushes the remaining buffer, and returns the anti-pop tail.
        """
        bytes_needed = self.fade_samples * 2 # 16-bit PCM = 2 bytes per sample
        if len(self.buffer) < bytes_needed:
            self.buffer.clear()
            self.is_playing = False
            return b""

        # Extract samples for fade
        samples = np.frombuffer(self.buffer[:bytes_needed], dtype=np.int16).astype(np.float32)
        # Compute Hann cosine half-window from 1.0 down to 0.0
        t = np.linspace(0, np.pi, len(samples))
        window = 0.5 * (1.0 + np.cos(t))
        faded_samples = (samples * window).astype(np.int16)

        # Clear active pending speech
        self.buffer.clear()
        self.is_playing = False
        return faded_samples.tobytes()


class LiveLinkFaceEncoder:
    """
    Encodes 52 ARKit blendshapes into Apple Live Link Face binary UDP datagrams
    for Unreal Engine 5 MetaHumans (port 11111).
    """
    @staticmethod
    def encode_frame(subject_name: str, blendshapes: Dict[str, float]) -> bytes:
        packet = bytearray()
        # Protocol version
        packet.append(6)

        # Pascal string for subject name (length prefix + utf-8 bytes)
        sub_bytes = subject_name.encode('utf-8')
        packet.extend(struct.pack('>B', len(sub_bytes)))
        packet.extend(sub_bytes)

        # Timecode (Frame, SubFrame, FPS numerator, FPS denominator)
        now = time.time()
        packet.extend(struct.pack('>IIII', int(now), int((now % 1) * 60), 60, 1))

        # 52 IEEE 754 floats
        packet.append(52)
        for name in ARKIT_BLENDSHAPES:
            val = float(blendshapes.get(name, 0.0))
            packet.extend(struct.pack('>f', val))

        return bytes(packet)


class VTubeStudioJsonRPC:
    """
    Generates InjectParameterDataRequest frames for Live2D models in VTube Studio (port 8001).
    """
    @staticmethod
    def make_mouth_frame(mouth_open: float, mouth_smile: float, face_angle_x: float = 0.0) -> Dict[str, Any]:
        return {
            "apiName": "VTubeStudioAPI",
            "apiVersion": "1.0",
            "requestID": f"tick_{int(time.time() * 1000)}",
            "messageType": "InjectParameterDataRequest",
            "data": {
                "mode": "set",
                "parameterValues": [
                    {"id": "MouthOpen", "value": round(float(mouth_open), 2), "weight": 1.0},
                    {"id": "MouthSmile", "value": round(float(mouth_smile), 2), "weight": 1.0},
                    {"id": "FaceAngleX", "value": round(float(face_angle_x), 2), "weight": 0.8}
                ]
            }
        }
