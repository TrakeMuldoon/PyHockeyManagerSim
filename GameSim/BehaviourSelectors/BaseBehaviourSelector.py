from typing import Any
from GameSim import GameSim


class BaseBehaviourSelector:
    def __init__(self, game_sim: "GameSim.GameSim") -> None:
        self.game_sim = game_sim

    def select_possessor_action_func(self) -> Any:
        raise Exception("Implement this yourself")
