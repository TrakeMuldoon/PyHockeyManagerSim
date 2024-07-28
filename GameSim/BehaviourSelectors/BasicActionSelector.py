from random import random
from GameSim import GameSim
from GameSim.BehaviourSelectors.BaseBehaviourSelector import BaseBehaviourSelector


class BasicActionSelector(BaseBehaviourSelector):
    SOUTH_DEFENSIVE_ZONES = {22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33}
    SOUTH_NEUTRAL_ZONES = {13, 14, 15, 16, 17, 18, 19, 20, 21}
    SOUTH_OFFENSIVE_ZONES = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    NORTH_DEFENSIVE_ZONES = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    NORTH_NEUTRAL_ZONES = {13, 14, 15, 16, 17, 18, 19, 20, 21}
    NORTH_OFFENSIVE_ZONES = {22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33}

    def __init__(self, game_sim: "GameSim.GameSim"):
        super().__init__(game_sim)
        d_res = game_sim.defensive_resolver
        self.DEFENSIVE_ACTIONS = {
            "FORWARD_PASS": {"weight": 10, "func": d_res.forward_pass},
            "LATERAL_PASS": {"weight": 10, "func": d_res.lateral_pass},
            "BACKWARD_PASS": {"weight": 5, "func": d_res.backward_pass},
            "CARRY": {"weight": 25, "func": d_res.carry},
            "CLEAR": {"weight": 25, "func": d_res.clear},
            "DUMP": {"weight": 25, "func": d_res.dump},
        }

        n_res = game_sim.neutral_resolver
        self.NEUTRAL_ACTIONS = {
            "FORWARD_PASS": {"weight": 10, "func": n_res.forward_pass},
            "LATERAL_PASS": {"weight": 15, "func": n_res.lateral_pass},
            "BACKWARD_PASS": {"weight": 5, "func": n_res.backward_pass},
            "CARRY": {"weight": 35, "func": n_res.carry},
            "DUMP": {"weight": 35, "func": n_res.dump},
        }

        o_res = game_sim.offensive_resolver
        self.OFFENSIVE_ACTIONS = {
            "OUTSIDE_PASS": {"weight": 25, "func": o_res.outside_pass},
            "CENTRAL_PASS": {"weight": 25, "func": o_res.central_pass},
            "SHOOT": {"weight": 25, "func": o_res.shoot},
            "CARRY": {"weight": 25, "func": o_res.carry},
        }

    def select_possessor_action_func(self):
        possessor = self.game_sim.puck_possessor
        zone_table = None
        if possessor in self.game_sim.north_team.dressed_players:
            zone_table = self._find_zone_table(
                self.NORTH_DEFENSIVE_ZONES, self.NORTH_NEUTRAL_ZONES, self.NORTH_OFFENSIVE_ZONES
            )
        else:
            zone_table = self._find_zone_table(
                self.SOUTH_DEFENSIVE_ZONES, self.SOUTH_NEUTRAL_ZONES, self.SOUTH_OFFENSIVE_ZONES
            )
        if not zone_table:
            raise Exception("what?")
        return self._select_random_action_from_weight_table(zone_table)

    def _find_zone_table(self, defence, neutral, offence):
        puck_zone = self.game_sim.puck_zone
        target_dict = None
        if puck_zone.value in defence:
            target_dict = self.DEFENSIVE_ACTIONS
        elif puck_zone.value in neutral:
            target_dict = self.NEUTRAL_ACTIONS
        elif puck_zone.value in offence:
            target_dict = self.OFFENSIVE_ACTIONS
        else:
            print("UNKNOWN ZONE BAD!")
        return target_dict

    @staticmethod
    def _select_random_action_from_weight_table(table):
        roll = random() * 100

        incremental_weight = 0

        for key in table:
            action = table[key]
            incremental_weight += action["weight"]
            if roll < incremental_weight:
                return action["func"]
