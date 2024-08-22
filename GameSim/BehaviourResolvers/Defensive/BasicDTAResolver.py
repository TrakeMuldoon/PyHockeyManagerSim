from typing import List
from GameSim.BehaviourResolvers.Defensive.DefensiveTeamActionResolver import (
    DefensiveTeamActionResolver,
)
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Zones import Zone


class BasicDTAResolver(DefensiveTeamActionResolver):
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

    def _try_up(self, zone_num: int) -> int:
        if zone_num < 30:
            zone_num += 3
        return zone_num

    def _try_back(self, zone_num: int) -> int:
        if zone_num > 3:
            zone_num -= 3
        return zone_num

    def _try_left(self, zone_num: int) -> int:
        l_c_r = (zone_num - 1) % 3
        if l_c_r != 0:
            return zone_num - 1
        else:
            return zone_num

    def _try_right(self, zone_num: int) -> int:
        l_c_r = (zone_num - 1) % 3
        if l_c_r != 2:
            return zone_num + 1
        else:
            return zone_num

    def move_up_left(self, player: Player) -> None:
        new_zone_num = self._try_up(player.zone.value)
        new_zone_num = self._try_left(new_zone_num)
        player.player_move(Zone(new_zone_num))

    def move_up(self, player: Player) -> None:
        new_zone_num = self._try_up(player.zone.value)
        player.player_move(Zone(new_zone_num))

    def move_up_right(self, player: Player) -> None:
        new_zone_num = self._try_up(player.zone.value)
        new_zone_num = self._try_right(new_zone_num)
        player.player_move(Zone(new_zone_num))

    def move_left(self, player: Player) -> None:
        new_zone_num = self._try_left(player.zone.value)
        player.player_move(Zone(new_zone_num))

    def move_right(self, player: Player) -> None:
        new_zone_num = self._try_right(player.zone.value)
        player.player_move(Zone(new_zone_num))

    def move_back_left(self, player: Player) -> None:
        new_zone_num = self._try_back(player.zone.value)
        new_zone_num = self._try_left(new_zone_num)
        player.player_move(Zone(new_zone_num))

    def move_back(self, player: Player) -> None:
        new_zone_num = self._try_back(player.zone.value)
        player.player_move(Zone(new_zone_num))

    def move_back_right(self, player: Player) -> None:
        new_zone_num = self._try_back(player.zone.value)
        new_zone_num = self._try_right(new_zone_num)
        player.player_move(Zone(new_zone_num))
