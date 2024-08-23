from random import Random
from GameSim import GameSim
from GameSim.BehaviourResolvers.Possessor.PossessorActionResolver import PossessorActionResolver
from GameSim.BehaviourSelectors.WeightedDictionary import WeightedDictionary
from GameSim.SupportClasses.Player import Player


class UnopposedPAResolver(PossessorActionResolver):
    def __init__(self, sim: "GameSim.GameSim"):
        super().__init__(sim)
        # faster to lookup than a series of if-statements
        self.action_dict = {
            "PASS_BACK": self.pass_back,
            "PASS_LATERAL": self.pass_lateral,
            "PASS_FORWARD": self.pass_forward,
            "CARRY_BACK": self.carry_back,
            "CARRY_LATERAL": self.carry_lateral,
            "CARRY_FORWARD": self.carry_forward,
            "SHOOT_LIGHT": self.shoot_light,
            "SHOOT_HARD": self.shoot_hard,
            "HOLD": self.hold,
        }
        self.player: Player = None  # type: ignore

    def get_supported_actions(self):
        return list(self.action_dict.keys())

    def resolve_action(self, action: str, player: Player):
        self.player = self.game_sim.puck_possessor
        action_func = self.action_dict[action]
        action_func()

    def pass_back(self):
        return "pass back"

    def pass_lateral(self):
        print("pass lateral")
        return "pass lateral"

    def pass_forward(self):
        print("pass forward")
        return "pass forward"

    carry_back_options = WeightedDictionary([("BL", 35), ("B", 30), ("BR", 35)])

    def carry_back(self):
        val = self.carry_back_options.get_weighted_random_value()
        match val:
            case "BL":
                self.move_back_left(self.player)
            case "B":
                self.move_back(self.player)
            case "BR":
                self.move_back_right(self.player)
        self.game_sim.puck_zone = self.player.zone
        return "carry_back"

    carry_lateral_options = WeightedDictionary(
        [("BL", 5), ("BR", 5), ("L", 40), ("R", 40), ("UL", 5), ("UR", 5)]
    )

    def carry_lateral(self):
        val = self.carry_forward_options.get_weighted_random_value()
        match val:
            case "BL":
                self.move_back_left(self.player)
            case "BR":
                self.move_back_right(self.player)
            case "L":
                self.move_left(self.player)
            case "R":
                self.move_right(self.player)
            case "UL":
                self.move_up_left(self.player)
            case "UR":
                self.move_up_right(self.player)
        self.game_sim.puck_zone = self.player.zone
        return "carry_lateral"

    carry_forward_options = WeightedDictionary([("UL", 35), ("U", 30), ("UR", 35)])

    def carry_forward(self):
        val = self.carry_forward_options.get_weighted_random_value()
        match val:
            case "UL":
                self.move_up_left(self.player)
            case "U":
                self.move_up(self.player)
            case "UR":
                self.move_up_right(self.player)
        self.game_sim.puck_zone = self.player.zone
        return "carry_forward"

    def shoot_light(self):
        print("shoot_light")
        return "shoot_light"

    def shoot_hard(self):
        print("shoot_hard")
        return "shoot_hard"

    def hold(self):
        print("hold")
        return "hold"
