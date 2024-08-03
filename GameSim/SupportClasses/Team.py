from random import random
from typing import List

from GameSim.SupportClasses.Goalie import Goalie
from GameSim.SupportClasses.Skater import Skater


class Team:
    def __init__(self):
        self.location: str = None  # type: ignore
        self.team_name: str = None  # type: ignore
        self.team_colour: str = None  # type: ignore
        self.skaters: List[Skater] = []
        self.goalies: List[Goalie] = []

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
