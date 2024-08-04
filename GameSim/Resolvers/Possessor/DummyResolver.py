from GameSim import GameSim
from GameSim.Resolvers.Possessor.PossessorActionResolver import PossessorActionResolver


class DummyResolver(PossessorActionResolver):
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

    def get_supported_actions(self):
        return [
            "PASS_BACK",
            "PASS_LATERAL",
            "PASS_FORWARD",
            "CARRY_BACK",
            "CARRY_LATERAL",
            "CARRY_FORWARD",
            "SHOOT_LIGHT",
            "SHOOT_HARD",
            "HOLD",
        ]

    def resolve_action(self, action: str):
        action_func = self.action_dict[action]
        action_func()

    def pass_back(self):
        print("pass back")
        return "pass back"

    def pass_lateral(self):
        print("pass lateral")
        return "pass lateral"

    def pass_forward(self):
        print("pass forward")
        return "pass forward"

    def carry_back(self):
        print("carry_back")
        return "carry_back"

    def carry_lateral(self):
        print("carry_lateral")
        return "carry_lateral"

    def carry_forward(self):
        print("carry_forward")
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
