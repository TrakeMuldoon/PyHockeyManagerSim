from abc import ABC, abstractmethod
from random import Random
from typing import TYPE_CHECKING, List
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Rink import Rink
from GameSim.SupportClasses.Zones import Zone

if TYPE_CHECKING:
    from GameSim import GameSim


class GenericResolver(ABC):
    def __init__(self, sim: "GameSim.GameSim", rand_seed: int = None):
        self.game_sim: "GameSim.GameSim" = sim
        if rand_seed:
            self.rand = Random(rand_seed)
        else:
            self.rand = Random()

    def does_support_action_list(self, required_actions: List[str]):
        supported_actions = self.get_supported_actions()
        for act in required_actions:
            if act not in supported_actions:
                return False
        return True

    @abstractmethod
    def get_supported_actions(self) -> List[str]:
        pass

    def move_up_left(self, player: Player) -> None:
        new_zone_num = Rink.left_ice(player.zone)
        new_zone_num = Rink.up_ice(new_zone_num)
        player.player_move(Zone(new_zone_num))

    def move_up(self, player: Player) -> None:
        new_zone_num = Rink.up_ice(player.zone)
        player.player_move(Zone(new_zone_num))

    def move_up_right(self, player: Player) -> None:
        new_zone_num = Rink.up_ice(player.zone)
        new_zone_num = Rink.right_ice(new_zone_num)
        player.player_move(Zone(new_zone_num))

    def move_left(self, player: Player) -> None:
        new_zone_num = Rink.left_ice(player.zone)
        player.player_move(Zone(new_zone_num))

    def move_right(self, player: Player) -> None:
        new_zone_num = Rink.right_ice(player.zone)
        player.player_move(Zone(new_zone_num))

    def move_back_left(self, player: Player) -> None:
        new_zone_num = Rink.down_ice(player.zone)
        new_zone_num = Rink.left_ice(new_zone_num)
        player.player_move(Zone(new_zone_num))

    def move_back(self, player: Player) -> None:
        new_zone_num = Rink.down_ice(player.zone)
        player.player_move(Zone(new_zone_num))

    def move_back_right(self, player: Player) -> None:
        new_zone_num = Rink.down_ice(player.zone)
        new_zone_num = Rink.right_ice(new_zone_num)
        player.player_move(Zone(new_zone_num))
