from random import random
from GameSim.Goalie import Goalie
from GameSim.Lines import OffensiveLine
from GameSim.Lines import DefensiveLine

class GameSim:
    SECONDS_IN_PERIOD = 60 * 20 # 1200

    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

        self.home_score = 0
        self.away_score = 0

        self.events = 0

        self.home_offence = OffensiveLine()
        self.home_defence = DefensiveLine()
        self.home_goalie : Goalie = None

        self.away_offence = OffensiveLine()
        self.away_defence = DefensiveLine()
        self.away_goalie : Goalie = None

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
        self.home_goalie = self.select_goalie_from_team(self.home_team)
        self.away_goalie = self.select_goalie_from_team(self.away_team)

        self.put_new_players_on_ice()

        # do opening faceoff
        while seconds_passed < GameSim.SECONDS_IN_PERIOD:
            self.events += 1
            # evaluate situation
            # check possession
                # no possession: race

                # check zone
                # check options
                # evaluate resolutions
            # move all other players
            # check for penalties
            self.print_game_time(period_num, seconds_passed)
            seconds_passed += int(random() * 4) + 3

            if seconds_passed > next_line_change_seconds:
                print("LINE CHANGE")
                self.put_new_players_on_ice()
                next_line_change_seconds += 59

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

    def put_new_players_on_ice(self):
        self.home_offence = self.home_team.next_offence()
        self.home_defence = self.home_team.next_defence()
        self.away_offence = self.away_team.next_offence()
        self.away_defence = self.away_team.next_defence()
        #self.print_players_on_ice()

    def print_players_on_ice(self):
        hd = self.home_defence
        ho = self.home_offence
        print(f"HOME\t\t{self.home_goalie.last_name}")
        print(f"\t\t{hd.left_defence.last_name}\t\t{hd.right_defence.last_name}")
        print(f"\t{ho.left_winger.last_name}\t{ho.centre.last_name}\t{ho.right_winger.last_name}")

        ad = self.away_defence
        ao = self.away_offence
        print(f"AWAY\t\t{self.away_goalie.last_name}")
        print(f"\t\t{ad.left_defence.last_name}\t\t{ad.right_defence.last_name}")
        print(f"\t{ao.left_winger.last_name}\t{ao.centre.last_name}\t{ao.right_winger.last_name}")

    @staticmethod
    def select_goalie_from_team(team):
        index = int(random() * len(team.goalies))
        return team.goalies[index]

    def simulate_shootout(self):
        pass