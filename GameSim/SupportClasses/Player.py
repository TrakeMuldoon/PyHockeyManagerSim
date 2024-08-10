import math
from random import random
from typing import TYPE_CHECKING
from GameSim.Generators.PlayerNameGenerator import PlayerNameGenerator
from GameSim.SupportClasses.Positions import Position
from GameSim.SupportClasses.Zones import Zone

if TYPE_CHECKING:
    from GameSim.SupportClasses.Team import Team


class Player:
    def __init__(self, team: "Team") -> None:
        self.first_name = PlayerNameGenerator.random_first_name()
        self.last_name = PlayerNameGenerator.random_last_name()
        self.preferred_num = int(random() * 98) + 1

        self.team: "Team" = team
        self.zone: Zone = Zone.NEU_CEN_FACEOFF
        self.position: Position = Position.EXTRA

    @staticmethod
    def generate_random_NHL_stat() -> float:
        stat = random() * 28
        stat = int(100 * stat)
        stat = stat / 100
        stat += 70
        return stat

    @staticmethod
    def round_sig(x, sig=2):
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)
