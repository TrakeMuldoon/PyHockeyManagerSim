from random import random

class GameSim:
    SECONDS_IN_PERIOD = 60 * 20
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

        self.home_score = 0
        self.away_score = 0

        self.events = 0

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
        self.put_goalie_on_ice()
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
            #  move all other players
            # check for penalties
            self.print_game_time(period_num, seconds_passed)
            seconds_passed += int(random() * 4) + 2

            if seconds_passed > next_line_change_seconds:
                print("LINECHANGE")
                self.put_new_players_on_ice()
                next_line_change_seconds += 59

    def print_game_time(self, period, seconds_passed):
        total_seconds_left = GameSim.SECONDS_IN_PERIOD - seconds_passed
        min_left = int(total_seconds_left / 60)
        sec_left = int(total_seconds_left) % 60

        min_passed = int(seconds_passed / 60)
        sec_passed = int(seconds_passed) % 60

        per = "1st" if period == 1 else "2nd" if period == 2 else "3rd"

        print(f"{min_left}:{sec_left:00} left. {min_passed}:{sec_passed:00} passed in the {per} period. {self.events}")

    def game_one_liner(self):
        pass

    def put_goalie_on_ice(self):
        pass

    def put_new_players_on_ice(self):
        pass

    def simulate_shootout(self):
        pass