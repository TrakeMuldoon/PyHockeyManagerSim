from __future__ import annotations
from random import random
from typing import Optional
from GameSim.ActionResult import ActionResult
from GameSim.BehaviourSelectors.Defensive.DefensiveTeamActionSelector import (
    DefensiveTeamActionSelector,
)
from GameSim.BehaviourSelectors.Offensive.OffensiveTeamActionSelector import (
    OffensiveTeamActionSelector,
)
from GameSim.BehaviourSelectors.Possessor.BasicActionSelector import BasicActionSelector
from GameSim.BehaviourSelectors.Possessor.PossessorActionSelector import PossessorActionSelector
from GameSim.BehaviourSelectors.Possessor.RandomActionSelector import RandomActionSelector
from GameSim.GameTeam import GameTeam
from GameSim.Resolvers.Defensive.DefensiveTeamActionResolver import DefensiveTeamActionResolver
from GameSim.Resolvers.Offensive.OffensiveTeamActionResolver import OffensiveTeamActionResolver
from GameSim.Resolvers.Possessor.DummyResolver import DummyResolver
from GameSim.Resolvers.Possessor.PossessorActionResolver import PossessorActionResolver
from GameSim.Resolvers.Race.PuckRaceResolver import PuckRaceResolver
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Zones import Zone


class GameSim:
    SECONDS_IN_PERIOD = 1200  # 60 * 20
    SKILL_FACTOR = 75

    def __init__(self, home_team, away_team, log_level=0) -> None:
        self.home_team: GameTeam = GameTeam(home_team)
        self.away_team: GameTeam = GameTeam(away_team)
        self.north_team: GameTeam = self.away_team

        self.home_score: int = 0
        self.away_score: int = 0

        self.events = 0

        self.period_time_left: int = 1200
        self.puck_zone: Zone = Zone.NEU_CEN_FACEOFF
        self.is_face_off = True
        self.puck_possessor: Player = None  # type: ignore

        self.puck_race_resolver: PuckRaceResolver = PuckRaceResolver(self)

        self.possessor_action_selector: PossessorActionSelector = RandomActionSelector(self)
        self.possessor_action_resolver: PossessorActionResolver = DummyResolver(self)
        if not self.possessor_action_resolver.does_support_action_list(
            self.possessor_action_selector.get_output_actions()
        ):
            raise Exception(
                "Possessor Action Resolver doesn't support all possible actions from Action Selector"
            )

        self.offensive_team_action_resolver: OffensiveTeamActionResolver = (
            OffensiveTeamActionResolver(self)
        )
        self.offensive_team_action_selector: OffensiveTeamActionSelector = (
            OffensiveTeamActionSelector(self)
        )

        self.defensive_team_action_resolver: DefensiveTeamActionResolver = (
            DefensiveTeamActionResolver(self)
        )
        self.defensive_team_action_selector: DefensiveTeamActionSelector = (
            DefensiveTeamActionSelector(self)
        )

    def set_up_for_period(self):
        # select 5 players and a goalie
        self.home_team.put_new_skaters_on_ice()
        self.home_team.set_new_period_zones(True)
        self.away_team.put_new_skaters_on_ice()
        self.away_team.set_new_period_zones(False)
        self.print_players_on_ice()

    def simulate_game(self, with_print_statements=True, playoffs=False):
        self.north_team = self.home_team
        self.set_up_for_period()
        self.simulate_period(1)

        self.north_team = self.away_team
        self.set_up_for_period()
        self.simulate_period(2)

        self.north_team = self.home_team
        self.set_up_for_period()
        self.simulate_period(3)

        if self.home_score == self.away_score:
            self.north_team = self.away_team
            self.set_up_for_period()
            self.simulate_period(4, True)

            if self.home_score == self.away_score:
                self.simulate_shootout()

        return self.game_result_one_liner()

    def simulate_period(self, period_num, extra_period=False):
        self.is_face_off = True
        seconds_passed = 0
        next_line_change_seconds = 60

        # do opening face_off
        while seconds_passed < GameSim.SECONDS_IN_PERIOD:
            self.events += 1
            self.simulate_next_event()
            # TODO: move all other players
            # TODO: PENALTY
            self.print_game_time(period_num, seconds_passed)
            seconds_passed += int(random() * 4) + 3

            if seconds_passed > next_line_change_seconds:
                if self.is_face_off:
                    print("LINE CHANGE")
                    self.home_team.put_new_skaters_on_ice()
                    self.away_team.put_new_skaters_on_ice()
                    next_line_change_seconds += 59

    def simulate_next_event(self) -> str:
        if self.is_face_off:
            # resolve face_off
            return self.simulate_face_off(
                self.home_team.active_offence.centre,
                self.away_team.active_offence.centre,
            )

        elif self.puck_possessor is None:
            # resolve race
            self.puck_race_resolver.resolve_race()

        else:
            # resolve possessed zone action
            result = self.resolve_puck_controlled_event()

        return "null"

    # TODO Delete this function?
    def simulate_shootout(self):
        pass

    # TODO Delete this function?
    def simulate_face_off(self, home_centre, away_centre) -> str:
        # home_centre.print_stats()
        # away_centre.print_stats()
        hc = home_centre
        home_val = (hc.puck_control + hc.stick_checking + hc.passing) / 3
        ac = away_centre
        away_val = (ac.puck_control + ac.stick_checking + ac.passing) / 3

        home_wins = self.determine_opposed_action_success(home_val, away_val)
        if home_wins:
            self.face_off_win(self.home_team)
            return f"Face off won by {home_centre.last_name} of the {self.home_team.team_name}"
        else:
            self.face_off_win(self.away_team)
            return f"Face off won by {away_centre.last_name} of the {self.away_team.team_name}"

    def face_off_win(self, team: GameTeam):
        roll = random()
        selected_player: Optional[Player] = None
        if roll < 0.25:
            selected_player = team.active_defence.left_defence
        elif roll < 0.50:
            selected_player = team.active_defence.right_defence
        elif roll < 0.7:
            selected_player = team.active_offence.left_winger

        elif roll < 0.9:
            selected_player = team.active_offence.right_winger
        else:
            selected_player = team.active_offence.centre

        self.puck_possessor = selected_player
        self.puck_zone = selected_player.zone
        self.is_face_off = False

    def resolve_puck_controlled_event(self) -> ActionResult:
        action = self.possessor_action_selector.select_action()
        action_result = self.possessor_action_resolver.resolve_action(action)
        return action_result

    ### (A - B + SF) / (2 * SF)(SF=75)
    @staticmethod
    def determine_opposed_action_success(active_player_skill_value, opposing_player_skill_value):
        act = active_player_skill_value
        opp = opposing_player_skill_value
        numerator = act - opp + GameSim.SKILL_FACTOR
        denominator = 2 * GameSim.SKILL_FACTOR
        odds = numerator / denominator

        roll = random()

        print(f"{act} vs {opp} : {odds} -> {roll}({roll < odds})")

        return roll < odds

    def print_game_time(self, period, seconds_passed):
        return
        total_seconds_left = GameSim.SECONDS_IN_PERIOD - seconds_passed

        min_left = int(total_seconds_left / 60)
        sec_left = int(total_seconds_left) % 60

        min_passed = int(seconds_passed / 60)
        sec_passed = int(seconds_passed) % 60

        per = "1st" if period == 1 else "2nd" if period == 2 else "3rd"

        print(f"{min_left:02}:{sec_left:02} left.", end="")
        print(f"{min_passed:02}:{sec_passed:02} passed in the {per} period. {self.events}")

    def print_players_on_ice(self):
        print("HOME", "")
        self.home_team.print_players_on_ice()

        print("AWAY", "")
        self.away_team.print_players_on_ice()

    def game_result_one_liner(self) -> str:
        home_score_text = f"{self.home_team.team_name}:{self.home_score}"
        away_score_text = f"{self.away_team.team_name}:{self.away_score}"
        if self.home_score == self.away_score:
            win_text = f"Game ends in a draw"
        elif self.home_score > self.away_score:
            win_text = f"{self.home_team.team_name} wins!"
        else:
            win_text = f"{self.away_team.team_name} are the winners."

        return f"Final Score: {home_score_text} and {away_score_text}, {win_text}"

    def yield_simulate_game(self) -> str:
        periods = [1, 2, 3]
        for period in periods:
            self.setup_standard_period(period)
            while self.period_time_left > 0:
                # increment timer
                self.events += 1
                seconds_passed = int(random() * 4) + 3
                self.period_time_left -= seconds_passed
                # simulate next event
                self.simulate_next_event()
                # TODO: move all other players
                # TODO: PENALTY
                yield f"{self.events}: {self.period_time_left}"
        # TODO: handle ties, and extra periods
        return self.game_result_one_liner()

    def setup_standard_period(self, period_num: int):
        # reset clock
        self.period_time_left: int = 1200

        # Flip team on North Side
        self.north_team = self.home_team if self.north_team == self.away_team else self.away_team

        # Set up opening face-off
        self.puck_zone: Zone = Zone.NEU_CEN_FACEOFF
        self.is_face_off = True
        self.puck_possessor: Player = None  # type: ignore

        # refresh players energy
        # TODO: ENERGY

        # refresh ice
        # TODO: ICE_QUALITY

        # set out lines (check penalties)
        # TODO: PENALTY
        self.home_team.put_new_skaters_on_ice(period_num)
        self.home_team.set_new_period_zones(self.home_team == self.north_team)
        self.away_team.put_new_skaters_on_ice(period_num)
        self.away_team.set_new_period_zones(self.away_team == self.north_team)
