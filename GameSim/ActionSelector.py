from random import random


class ActionSelector:
    SOUTH_DEFENSIVE_ZONES = {22, 23, 24, 25, 26, 27, 29, 31, 32, 33}
    SOUTH_NEUTRAL_ZONES = {13, 14, 15, 17, 19, 20, 21}
    SOUTH_OFFENSIVE_ZONES = {1, 2, 3, 5, 7, 8, 9, 10, 11, 12}

    NORTH_DEFENSIVE_ZONES = {1, 2, 3, 5, 7, 8, 9, 10, 11, 12}
    NORTH_NEUTRAL_ZONES = {13, 14, 15, 17, 19, 20, 21}
    NORTH_OFFENSIVE_ZONES = {22, 23, 24, 25, 26, 27, 29, 31, 32, 33}

    # def __init__(self, game_sim: GameSim):
    def __init__(self, game_sim):
        self.game_sim = game_sim
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

    def select_action(self):
        possessor = self.game_sim.puck_possessor
        zone_table = None
        if possessor in self.game_sim.north_team.dressed_players:
            zone_table = self.find_zone_table(
                self.NORTH_DEFENSIVE_ZONES, self.NORTH_NEUTRAL_ZONES, self.NORTH_OFFENSIVE_ZONES
            )
        else:
            zone_table = self.find_zone_table(
                self.SOUTH_DEFENSIVE_ZONES, self.SOUTH_NEUTRAL_ZONES, self.SOUTH_OFFENSIVE_ZONES
            )
        return self.select_random_action_from_weight_table(zone_table)

    def find_zone_table(self, defence, neutral, offence):
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
    def select_random_action_from_weight_table(table):
        roll = random() * 100

        incremental_weight = 0

        for key in table:
            action = table[key]
            incremental_weight += action["weight"]
            if roll < incremental_weight:
                return action["func"]


"""
- Pass
  Percentage choice based on STRATEGY
  Forward, Lateral ( including current zone), Backwards
  OUTCOMES
  Passed, missed (lost control), interception
- Breakout (if available)
  Attempt to forward pass with a higher probabilty of leaving the zone, and lower probability of completed pass
  OUTCOMES
  Forward Pass, Clear Zone (opposition control), Clear Zone (No possessor), interception
- Carry
  Percentage choice based on STRATEGY
  Forward, Lateral (including current zone), backwards
  OUTCOMES
  Move Zone, Lose Control (no possessor), interception
- Clear
  Very High probabilty of leaving the zone, probability of icing , depending on factors
  OUTCOMES - push puck past blueline
  Clear Zone (No controller), Clear Zone (opposition), Icing, Interception
"""
