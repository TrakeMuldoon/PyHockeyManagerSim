from random import random
from GameSim.SupportClasses.Goalie import Goalie
from GameSim.SupportClasses.Lines import DefensiveLine, OffensiveLine
from GameSim.SupportClasses.Zones import Zones
from GameSim.Team import Team


class GameTeam:
    def __init__(self, team: Team):
        self.dressed_goalies = team.goalies
        self.dressed_players = team.players
        self.num_dressed_players = len(self.dressed_players)

        self.active_offence = OffensiveLine()
        self.active_defence = DefensiveLine()
        self.goalie: Goalie = self.select_goalie()

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
        print(f"\t\t{self.short_player(de.left_defence)}\t\t{self.short_player(de.right_defence)}")
        print(
            f"\t{self.short_player(of.left_winger)}\t{self.short_player(of.centre)}\t{self.short_player(of.right_winger)}"
        )

    @staticmethod
    def short_player(player):
        return f"[{player.last_name}|{player.zone.value}]"

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

    def set_new_period_zones(self, top: bool):
        if top:
            self.active_offence.left_winger.zone = Zones.TOP_CENTRE_NEUTRAL
            self.active_offence.right_winger.zone = Zones.TOP_CENTRE_NEUTRAL
            self.active_offence.centre.zone = Zones.CENTRE_ICE
            self.active_defence.left_defence.zone = Zones.TOP_RIGHT_NEUTRAL
            self.active_defence.right_defence.zone = Zones.TOP_LEFT_NEUTRAL
        else:
            self.active_offence.left_winger.zone = Zones.BOTTOM_CENTRE_NEUTRAL
            self.active_offence.right_winger.zone = Zones.BOTTOM_CENTRE_NEUTRAL
            self.active_offence.centre.zone = Zones.CENTRE_ICE
            self.active_defence.left_defence.zone = Zones.BOTTOM_LEFT_NEUTRAL
            self.active_defence.right_defence.zone = Zones.BOTTOM_RIGHT_NEUTRAL
