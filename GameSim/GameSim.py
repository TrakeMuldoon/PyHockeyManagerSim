from random import random
from GameSim.GameTeam import GameTeam
from GameSim.Goalie import Goalie
from GameSim.Player import Player
from GameSim.Lines import OffensiveLine
from GameSim.Lines import DefensiveLine
from GameSim.Zones import Zones

class GameSim:
    SECONDS_IN_PERIOD = 60 * 20 # 1200

    def __init__(self, home_team, away_team):
        self.home_team = GameTeam(home_team)
        self.away_team = GameTeam(away_team)

        self.home_score = 0
        self.away_score = 0

        self.events = 0

        self.puck_zone : Zones = Zones.CENTRE_ICE
        self.face_off = True
        self.puck_possessor : Player = None

    def simulate_game(self, with_print_statements=True, playoffs=False):
        self.simulate_period(1)
        self.simulate_period(2)
        self.simulate_period(3)

        if self.home_score == self.away_score:
            self.simulate_period(4, True)

            if self.home_score == self.away_score:
                self.simulate_shootout()

        return self.game_one_liner()

    def simulate_period(self, period_num, extra_period=False):
        seconds_passed = 0
        next_line_change_seconds = 60

        # select 5 players and a goalie
        self.home_team.put_new_players_on_ice()
        self.home_team.set_new_period_zones(True)
        self.away_team.put_new_players_on_ice()
        self.away_team.set_new_period_zones(False)
        self.print_players_on_ice()

        # do opening faceoff
        while seconds_passed < GameSim.SECONDS_IN_PERIOD:
            self.events += 1
            self.simulate_next_event()
            self.print_game_time(period_num, seconds_passed)
            seconds_passed += int(random() * 4) + 3

            if seconds_passed > next_line_change_seconds:
                print("LINE CHANGE")
                if self.face_off:
                    self.home_team.put_new_players_on_ice()
                    self.away_team.put_new_players_on_ice()
                    next_line_change_seconds += 59

    def simulate_next_event(self):
        if self.face_off:
            # resolve faceoff
            excep = 1 / 0

        elif self.puck_possessor is None:
            # resolve race
            excep = 1 / 0

        else:
            # resolve possessed zone action
            # check zone
            # check options
            # evaluate resolutions
            execp = 1 / 0
        # move all other players
        # check for penalties

    def print_game_time(self, period, seconds_passed):
        total_seconds_left = GameSim.SECONDS_IN_PERIOD - seconds_passed
        min_left = int(total_seconds_left / 60)
        sec_left = int(total_seconds_left) % 60

        min_passed = int(seconds_passed / 60)
        sec_passed = int(seconds_passed) % 60

        per = "1st" if period == 1 else "2nd" if period == 2 else "3rd"

        print(f"{min_left:02}:{sec_left:02} left. {min_passed:02}:{sec_passed:02} passed in the {per} period. {self.events}")

    def game_one_liner(self):
        pass

    def print_players_on_ice(self):
        print("HOME", "")
        self.home_team.print_players_on_ice()

        print("AWAY","")
        self.away_team.print_players_on_ice()

    def simulate_shootout(self):
        pass
