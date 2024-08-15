from abc import abstractmethod
from typing import List

from GameSim import GameSim


class DefensiveTeamActionSelector:
    def __init__(self, sim: "GameSim.GameSim"):
        pass

    @abstractmethod
    def select_action(self):
        pass

    @abstractmethod
    def get_output_actions(self) -> List[str]:
        pass
