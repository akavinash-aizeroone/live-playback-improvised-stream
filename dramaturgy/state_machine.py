"""
Dramaturgy Module: Theatrical State Machine uniting Boal's Forum Theatre,
Fox's Playback Theatre, and Johnstone's Status Seesaw & Re-incorporation Engine.
"""
import copy
from typing import Dict, List, Any, Optional

class JohnstoneStatusSeesaw:
    """
    Manages relative status (1.0 to 10.0) between primary improvisational agents.
    Status is never absolute; an assertive move by Agent A lowers Agent B's status.
    """
    def __init__(self, initial_status_a: float = 7.0, initial_status_b: float = 3.0):
        self.status_a = initial_status_a
        self.status_b = initial_status_b

    def apply_transaction(self, speaker: str, move_type: str, delta: float = 1.0) -> Dict[str, float]:
        if speaker == "AGENT_A":
            if move_type == "RAISE_SELF":
                self.status_a = min(10.0, self.status_a + delta)
                self.status_b = max(1.0, self.status_b - (delta * 0.7))
            elif move_type == "LOWER_SELF":
                self.status_a = max(1.0, self.status_a - delta)
                self.status_b = min(10.0, self.status_b + (delta * 0.7))
        else: # AGENT_B
            if move_type == "RAISE_SELF":
                self.status_b = min(10.0, self.status_b + delta)
                self.status_a = max(1.0, self.status_a - (delta * 0.7))
            elif move_type == "LOWER_SELF":
                self.status_b = max(1.0, self.status_b - delta)
                self.status_a = min(10.0, self.status_a + (delta * 0.7))

        return {"status_a": round(self.status_a, 2), "status_b": round(self.status_b, 2)}


class ReincorporationLedger:
    """
    Prevents narrative drift and entropy explosion by maintaining an episodic
    graph of entities, names, objects, and promises introduced during the Platform.
    """
    def __init__(self):
        self.ledger: List[Dict[str, Any]] = []

    def record_element(self, entity: str, category: str, introduced_turn: int):
        self.ledger.append({
            "entity": entity,
            "category": category, # e.g. "PROP", "RELATIONSHIP", "VOW"
            "turn": introduced_turn,
            "resolved": False
        })

    def get_dangling_elements(self) -> List[str]:
        return [item["entity"] for item in self.ledger if not item["resolved"]]

    def resolve_element(self, entity: str):
        for item in self.ledger:
            if item["entity"].lower() == entity.lower():
                item["resolved"] = True


class BoalForumGovernor:
    """
    Augusto Boal's Forum Theatre Engine:
    - Maintains scene snapshots for rollback on "STOP!" intervention.
    - Anti-Magical Gate evaluates whether spect-actor tactics are realistic.
    - Mathematical Oppressor Resistance Model.
    """
    def __init__(self, systemic_power: float = 0.85, concession_threshold: float = 0.25):
        self.systemic_power = systemic_power
        self.concession_threshold = concession_threshold
        self.snapshot_history: List[Dict[str, Any]] = []
        self.current_state: str = "BASELINE_RUN" # BASELINE_RUN, JOKER_HALT, TACTICAL_TRIAL

    def save_checkpoint(self, turn_number: int, dialogue_history: List[Any], world_state: Dict[str, Any]):
        snapshot = {
            "turn": turn_number,
            "history": copy.deepcopy(dialogue_history),
            "world": copy.deepcopy(world_state)
        }
        self.snapshot_history.append(snapshot)
        if len(self.snapshot_history) > 10:
            self.snapshot_history.pop(0)

    def trigger_stop(self) -> Optional[Dict[str, Any]]:
        self.current_state = "JOKER_HALT"
        if not self.snapshot_history:
            return None
        # Return the pre-crisis rollback snapshot
        return copy.deepcopy(self.snapshot_history[-1])

    def evaluate_oppressor_resistance(self, tactic_leverage: float, solidarity_score: float) -> Dict[str, Any]:
        """
        Sigmoidal Oppressor Resistance:
        R_opp = sigmoid(W_pow * P_sys - W_lev * L_tac - W_sol * S_allies)
        """
        import numpy as np
        z = (2.5 * self.systemic_power) - (3.0 * tactic_leverage) - (1.5 * solidarity_score)
        resistance = 1.0 / (1.0 + np.exp(-z))
        concession_granted = resistance <= self.concession_threshold

        return {
            "resistance_score": round(float(resistance), 3),
            "concession_granted": concession_granted,
            "response_type": "CAPITULATE" if concession_granted else "RESIST_AND_COUNTER"
        }
