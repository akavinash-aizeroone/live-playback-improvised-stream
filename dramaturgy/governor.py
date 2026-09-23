"""
Dramaturgy Module: Closed-Loop PID Tension Governor.
Stabilizes the dramatic tension curve to avoid narrative fatigue or flat boredom.
"""
import time

class PIDTensionGovernor:
    """
    Closed-loop controller adjusting dramatic pacing by comparing
    observed scene tension against target Freytag/Spine tension.
    """
    def __init__(self, kp: float = 0.8, ki: float = 0.05, kd: float = 0.15, setpoint: float = 0.60):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.integral = 0.0
        self.last_error = 0.0
        self.last_time = time.time()

    def update(self, observed_tension: float) -> dict:
        now = time.time()
        dt = max(0.01, now - self.last_time)

        error = self.setpoint - observed_tension
        self.integral += error * dt
        # Anti-windup clamping
        self.integral = max(-1.0, min(1.0, self.integral))
        derivative = (error - self.last_error) / dt

        control_output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

        self.last_error = error
        self.last_time = now

        # Translate control_output into dramaturgical action directives
        pacing_directive = "MAINTAIN"
        if control_output > 0.25:
            pacing_directive = "INJECT_TILT_OR_STATUS_CLASH"
        elif control_output < -0.25:
            pacing_directive = "INJECT_RELIEF_OR_SOMATIC_PAUSE"

        return {
            "error": round(error, 3),
            "control_output": round(control_output, 3),
            "directive": pacing_directive,
            "tempo_multiplier": round(max(0.7, min(1.4, 1.0 + control_output * 0.3)), 2)
        }
