from random import random
from typing import List

from GameSim.SupportClasses.Goalie import Goalie
from GameSim.SupportClasses.Skater import Skater


class Team:
    location: str
    team_name: str
    team_colour: str
    skaters: List[Skater] = []
    goalies: List[Goalie] = []

    def __init__(self):
        pass

    def print_team(self):
        print(f"{self.team_name} from {self.location}")
        print("PLAYERS")
        for skater in self.skaters:
            print("\t", end="")
            skater.print_stats()
        for goalie in self.goalies:
            print("\t", end="")
            goalie.print_stats()

    def select_goalie_from_team(self):
        index = int(random() * len(self.goalies))
        return self.goalies[index]
