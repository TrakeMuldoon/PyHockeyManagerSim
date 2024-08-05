from abc import ABC, abstractmethod
from typing import List
from GameSim import GameSim


class OffensiveTeamActionSelector(ABC):
    def __init__(self, sim: "GameSim.GameSim"):
        self.game_sim = sim
        pass

    @abstractmethod
    def select_action(self):
        pass

    @abstractmethod
    def get_output_actions(self) -> List[str]:
        pass
