from typing import List

from GameSim.BehaviourSelectors.Defensive.DefensiveTeamActionSelector import DefensiveTeamActionSelector
from GameSim.BehaviourSelectors.WeightedDictionary import WeightedDictionary


class RandomDTASelector(DefensiveTeamActionSelector):
    def __init__(self, sim: "GameSim"):
        super().__init__(sim)
        weights = [
            ("Move_UpLeft", 12.5),
            ("Move_UpIce", 12.5),
            ("Move_UpRight", 12.5),
            ("Move_Left", 12.5),
            ("Move_Right", 12.5),
            ("Move_BackLeft", 12.5),
            ("Move_Back", 12.5),
            ("Move_BackRight", 12.5),
        ]
        self.actions_dict: WeightedDictionary = WeightedDictionary(weights)

    def get_output_actions(self) -> List[str]:
        return list(self.actions_dict.keys())

    def select_action(self):
        return self.actions_dict.get_weighted_random_value()
