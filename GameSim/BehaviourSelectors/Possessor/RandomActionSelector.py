from random import random
from typing import List
from GameSim.BehaviourSelectors.Possessor.PossessorActionSelector import PossessorActionSelector


class RandomActionSelector(PossessorActionSelector):
    def __init__(self, sim: "GameSim.GameSim"):
        super().__init__(sim)
        self.action_table = {
            "PASS_BACK": 12,
            "PASS_LATERAL": 12,
            "PASS_FORWARD": 12,
            "CARRY_BACK": 12,
            "CARRY_LATERAL": 12,
            "CARRY_FORWARD": 11,
            "SHOOT_LIGHT": 11,
            "SHOOT_HARD": 11,
            "HOLD": 7,
        }

    def select_action(self) -> str:
        roll = random() * 100

        incremental_weight = 0
        for key in self.action_table.keys():
            incremental_weight += self.action_table[key]
            if roll < incremental_weight:
                return key
        raise Exception("Unable to select key")

    def get_output_actions(self) -> List[str]:
        return [
            "PASS_BACK",
            "PASS_LATERAL",
            "PASS_FORWARD",
            "CARRY_BACK",
            "CARRY_LATERAL",
            "CARRY_FORWARD",
            "SHOOT_LIGHT",
            "SHOOT_HARD",
            "HOLD",
        ]
