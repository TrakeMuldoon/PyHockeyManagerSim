from random import random
from GameSim.Generators.PlayerNameGenerator import PlayerNameGenerator
from GameSim.Positions import Positions
from GameSim.Zones import Zones
import math


class Player:
    def __init__(self):
        self.speed = self.generate_random_NHL_stat()
        self.endurance = self.generate_random_NHL_stat()

        self.short_shooting = self.generate_random_NHL_stat()
        self.long_shooting = self.generate_random_NHL_stat()
        self.puck_control = self.generate_random_NHL_stat()
        self.passing = self.generate_random_NHL_stat()

        self.shot_blocking = self.generate_random_NHL_stat()
        self.stick_checking = self.generate_random_NHL_stat()

        self.first_name = PlayerNameGenerator.random_first_name()
        self.last_name = PlayerNameGenerator.random_last_name()

        self.position = Positions(int(random() * 5) + 2)

        self.zone: Zones = Zones.CENTRE_ICE

    def generate_random_NHL_stat(self):
        stat = random() * 28
        stat = int(100 * stat)
        stat = stat / 100
        stat += 70
        return stat

    @staticmethod
    def round_sig(x, sig=2):
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

    def print_stats(self):
        name = f"{self.first_name} {self.last_name} ({str(self.position)[10:]})"
        player = f"SPD:{self.speed}\tEND:{self.endurance}"
        offence = f"WRST:{self.short_shooting}\tSLAP:{self.long_shooting}\tPC:{self.puck_control:<9}PASS:{self.passing}"
        defence = f"BLK:{self.shot_blocking}\tSCHK:{self.stick_checking}"
        print(f"{name:<40}>>\t{player}\t|\t{offence}\t|\t{defence}")


'''
Athletic
- Speed (to resolve races)
- Endurance (how their stats flag over the course of the game)

Offensive
- Puck Control (to resolve dekes)
- Short Shooting (Zones close to the net)
- Long Shooting (Zones far from the net)
- Passing

Defensive
- Shot Blocking (to oppose Long Shooting)
- Stick-Checking (to oppose puck control and passing)

'''

