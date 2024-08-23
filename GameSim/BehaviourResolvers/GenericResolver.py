from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Zones import Zone

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
