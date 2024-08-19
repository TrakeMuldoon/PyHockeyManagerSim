from abc import ABC, abstractmethod
from typing import List
from GameSim import GameSim


class PossessorActionSelector(ABC):
    game_sim: "GameSim.GameSim"

    def __init__(self, sim: "GameSim.GameSim"):
        self.game_sim = sim

    @abstractmethod
    def select_action(self):
        pass

    @abstractmethod
    def get_output_actions(self) -> List[str]:
        pass
