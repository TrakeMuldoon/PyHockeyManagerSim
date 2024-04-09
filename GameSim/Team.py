from random import random
from GameSim.Lines import OffensiveLine
from GameSim.Lines import DefensiveLine
from GameSim.Goalie import Goalie

class Team:
    def __init__(self):
        self.location = None
        self.team_name = None
        self.players = []
        self.goalies = []


    def print_team(self):
        print(f"{self.team_name} from {self.location}")
        print("PLAYERS")
        for player in self.players:
            print("\t", end='')
            player.print_stats()
        for goalie in self.goalies:
            print("\t", end='')
            goalie.print_stats()

    def select_goalie_from_team(self):
        index = int(random() * len(self.goalies))
        return self.goalies[index]