from typing import List
from GameSim import GameSim
from GameSim.ActionResult import ActionResult


class PossessorActionResolver:
    def __init__(self, sim: "GameSim.GameSim"):
        pass

    def does_support_action_list(self, required_actions: List[str]):
        supported_actions = self.get_supported_actions()
        for act in required_actions:
            if act not in supported_actions:
                return False
        return True

    def get_supported_actions(self) -> List[str]:
        raise Exception("Implement this for yourself, Bub.")

    def resolve_action(self, action: str) -> ActionResult:
        raise Exception("Implement this for yourself, Pal.")
