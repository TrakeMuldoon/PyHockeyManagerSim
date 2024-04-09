from GameSim.Team import Team
from GameSim.Goalie import Goalie
from random import random
from GameSim.Lines import OffensiveLine
from GameSim.Lines import DefensiveLine

class GameTeam:
    def __init__(self, team : Team):
        self.dressed_goalies = team.goalies
        self.dressed_players = team.players
        self.num_dressed_players = len(self.dressed_goalies)

        self.active_offence = OffensiveLine()
        self.active_defence = DefensiveLine()
        self.goalie : Goalie = self.select_goalie()

    def put_new_players_on_ice(self):
        self.active_offence = self.next_offence()
        self.active_defence = self.next_defence()

    def select_goalie(self):
        index = int(random() * len(self.dressed_goalies))
        return self.dressed_goalies[index]

    def print_players_on_ice(self):
        of = self.active_offence
        de = self.active_defence
        print(f"\t\t{self.goalie.last_name}")
        print(f"\t\t{de.left_defence.last_name}\t\t{de.right_defence.last_name}")
        print(f"\t{of.left_winger.last_name}\t{of.centre.last_name}\t{of.right_winger.last_name}")

    def next_offence(self):
        index = int(random() * self.num_dressed_players)
        line = OffensiveLine()
        line.left_winger = self.dressed_players[index]
        line.centre = self.dressed_players[(index + 1) % self.num_dressed_players]
        line.right_winger = self.dressed_players[(index + 2) % self.num_dressed_players]
        return line

    def next_defence(self):
        index = int(random() * self.num_dressed_players)
        line = DefensiveLine()
        line.left_defence = self.dressed_players[index]
        line.right_defence = self.dressed_players[(index + 1) % self.num_dressed_players]
        return line