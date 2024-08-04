from typing import List
from GameSim import GameSim


class PossessorActionSelector:
    game_sim: "GameSim.GameSim"

    def __init__(self, sim: "GameSim.GameSim"):
        self.game_sim = sim
        pass

    def select_action(self):
        raise Exception("You must implement this in your child-class. Doofus.")

    def get_output_actions(self) -> List[str]:
        raise Exception("You must implement this in your child-class. Dimples.")
