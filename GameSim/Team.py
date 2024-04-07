from random import random
from GameSim.Lines import OffensiveLine
from GameSim.Lines import DefensiveLine

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

    def next_offence(self):
        num_players = len(self.players) # TODO: optimize this to set "len" at the beginning of the game.
        index = int(random() * num_players)
        line = OffensiveLine()
        line.left_winger = self.players[index]
        line.centre = self.players[(index + 1) % num_players]
        line.right_winger = self.players[(index + 2) % num_players]
        return line

    def next_defence(self):
        num_players = len(self.players) # TODO: optimize this to set "len" at the beginning of the game.
        index = int(random() * num_players)
        line = DefensiveLine()
        line.left_defence = self.players[index]
        line.right_defence = self.players[(index + 1) % num_players]
        return line
