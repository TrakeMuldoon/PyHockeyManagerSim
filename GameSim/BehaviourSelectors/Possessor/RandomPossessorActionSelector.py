from typing import List
from GameSim.BehaviourSelectors.Possessor.PossessorActionSelector import PossessorActionSelector
from GameSim.BehaviourSelectors.WeightedDictionary import WeightedDictionary


class RandomPossessorActionSelector(PossessorActionSelector):
    def __init__(self, sim: "GameSim"):
        super().__init__(sim)
        weights = [
            ("PASS_BACK", 12.0),
            ("PASS_LATERAL", 12.0),
            ("PASS_FORWARD", 12.0),
            ("CARRY_BACK", 12.0),
            ("CARRY_LATERAL", 12.0),
            ("CARRY_FORWARD", 11.0),
            ("SHOOT_LIGHT", 11.0),
            ("SHOOT_HARD", 11.0),
            ("HOLD", 7.0),
        ]

        self.action_table: WeightedDictionary = WeightedDictionary(weights)

    def select_action(self) -> str:
        return self.action_table.get_weighted_random_value()

    def get_output_actions(self) -> List[str]:
        return self.action_table.keys()
