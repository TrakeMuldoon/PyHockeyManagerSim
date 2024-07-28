from random import random
from GameSim.SupportClasses.Goalie import Goalie
from GameSim.SupportClasses.Lines import DefensiveLine, OffensiveLine
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Zones import Zone
from GameSim.Team import Team


def _reverse_player_zone(player: Player):
    player.zone = player.zone.get_reverse_zone()


class GameTeam:
    def __init__(self, team: Team):
        self.dressed_goalies = team.goalies
        self.dressed_players = team.players
        self.num_dressed_players = len(self.dressed_players)

        self.active_offence: OffensiveLine = OffensiveLine()
        self.active_defence: DefensiveLine = DefensiveLine()
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
        self.active_offence.left_winger.zone = Zone.NEU_CEN_LEFT
        self.active_offence.right_winger.zone = Zone.NEU_CEN_RIGHT
        self.active_offence.centre.zone = Zone.NEU_CEN_FACEOFF
        self.active_defence.left_defence.zone = Zone.NEU_DEF_LEFT_DOT
        self.active_defence.right_defence.zone = Zone.NEU_DEF_RIGHT_DOT
        if top:
            self._reverse_player_zones()

    def _reverse_player_zones(self):
        _reverse_player_zone(self.active_offence.left_winger)
        _reverse_player_zone(self.active_offence.right_winger)
        _reverse_player_zone(self.active_offence.centre)
        _reverse_player_zone(self.active_defence.left_defence)
        _reverse_player_zone(self.active_defence.left_defence)
