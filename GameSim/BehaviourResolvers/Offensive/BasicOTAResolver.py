from typing import TYPE_CHECKING, List
from GameSim.BehaviourResolvers.Offensive.OffensiveTeamActionResolver import (
    OffensiveTeamActionResolver,
)
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Zones import Zone

if TYPE_CHECKING:
    from GameSim import GameSim


class BasicOTAResolver(OffensiveTeamActionResolver):
    def __init__(self, sim: "GameSim.GameSim"):
        super().__init__(sim)
        self.actions_dict = {
            "Move_UpLeft": self.move_up_left,
            "Move_UpIce": self.move_up,
            "Move_UpRight": self.move_up_right,
            "Move_Left": self.move_left,
            "Move_Right": self.move_right,
            "Move_BackLeft": self.move_back_left,
            "Move_Back": self.move_back,
            "Move_BackRight": self.move_back_right,
        }

    def get_supported_actions(self) -> List[str]:
        return list(self.actions_dict)

    # TODO Rename this function to indicate it mutates and returns None
    def resolve_action(self, action: str, player: Player) -> None:
        action_func = self.actions_dict[action]
        action_func(player)
