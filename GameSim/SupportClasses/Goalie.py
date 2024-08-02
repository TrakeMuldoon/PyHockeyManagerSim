import math
from random import random
from GameSim.SupportClasses.Player import Player, Position
from GameSim.SupportClasses.Team import Team
from GameSim.SupportClasses.Zones import Zone


class Goalie(Player):
    def __init__(self, team: Team):
        super().__init__(team)
        self.pads = self.generate_random_NHL_stat()
        self.stick = self.generate_random_NHL_stat()

        self.glove = self.generate_random_NHL_stat()
        self.blocker = self.generate_random_NHL_stat()

        self.passing = self.generate_random_NHL_stat()

        self.position = Position.GOALIE
        self.zone = Zone.DEF_CREASE

    def generate_random_NHL_stat(self):
        stat = random() * 28
        stat = self.round_sig(stat, 3)
        stat += 70
        return stat

    def round_sig(self, x, sig=2):
        return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

    def print_stats(self):
        name = f"{self.first_name} {self.last_name} ({str(self.position)[10:]})"
        low = f"PADS:{self.pads}\tSTK:{self.stick}"
        high = f"GLV:{self.glove}\tBLKR:{self.blocker}\tPASS:{self.passing}"
        print(f"{name:<40}>>\t{low}\t|\t{high}")
