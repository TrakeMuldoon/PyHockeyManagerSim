import math
from random import random
from GameSim.Generators.PlayerNameGenerator import PlayerNameGenerator
from GameSim.SupportClasses.Positions import Position
from GameSim.SupportClasses.Zones import Zone


class Player:
    first_name: str = PlayerNameGenerator.random_first_name()
    last_name: str = PlayerNameGenerator.random_last_name()
    preferred_num: int = int(random() * 98) + 1

    zone: Zone
    position: Position

    def __init__(self) -> None:
        self.first_name = PlayerNameGenerator.random_first_name()
        self.last_name = PlayerNameGenerator.random_last_name()
        self.preferred_num = int(random() * 98) + 1

        self.zone = Zone.NEU_CEN_FACEOFF

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
