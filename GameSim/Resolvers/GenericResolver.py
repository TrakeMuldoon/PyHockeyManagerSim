from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from GameSim import GameSim


class GenericResolver(ABC):
    def __init__(self, sim: "GameSim.GameSim"):
        self.game_sim: "GameSim.GameSim" = sim

    def does_support_action_list(self, required_actions: List[str]):
        supported_actions = self.get_supported_actions()
        for act in required_actions:
            if act not in supported_actions:
                return False
        return True

    @abstractmethod
    def get_supported_actions(self) -> List[str]:
        pass
