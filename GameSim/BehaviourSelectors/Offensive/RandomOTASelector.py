from typing import List
from GameSim.BehaviourSelectors.Offensive.OffensiveTeamActionSelector import (
    OffensiveTeamActionSelector,
)
from GameSim.BehaviourSelectors.WeightedDictionary import WeightedDictionary


class RandomOTASelector(OffensiveTeamActionSelector):
    def __init__(self, sim: "GameSim"):
        super().__init__(sim)
        weights = [
            ("Move_N", 12.5),
            ("Move_NE", 12.5),
            ("Move_E", 12.5),
            ("Move_SE", 12.5),
            ("Move_S", 12.5),
            ("Move_SW", 12.5),
            ("Move_W", 12.5),
            ("Move_NW", 12.5),
        ]
        self.actions_dict: WeightedDictionary = WeightedDictionary(weights)

    def get_output_actions(self) -> List[str]:
        return list(self.actions_dict.keys())

    def select_action(self):
        return self.actions_dict.get_weighted_random_value()
