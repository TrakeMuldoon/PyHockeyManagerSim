from random import Random
from GameSim import GameSim
from GameSim.ActionResult import ActionResult
from GameSim.BehaviourResolvers.Possessor.PossessorActionResolver import PossessorActionResolver
from GameSim.BehaviourSelectors.WeightedDictionary import WeightedDictionary
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Rink import Rink


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

    def resolve_action(self, action: str, player: Player) -> ActionResult:
        self.player = self.game_sim.puck_possessor
        action_func = self.action_dict[action]
        res = action_func()
        return res

    def pass_back(self) -> ActionResult:
        teammates = self.game_sim.offensive_team.get_skaters_on_ice()
        my_row = Rink.get_row(self.player.zone)
        down_ice = [t for t in teammates if Rink.get_row(t.zone) < my_row]
        lateral = [t for t in teammates if t != self.player and Rink.get_row(t.zone) == my_row]

        target_player = None
        if down_ice:
            selection = self.rand.randint(0, len(down_ice) - 1)
            target_player = down_ice[selection]
        elif lateral:
            selection = self.rand.randint(0, len(lateral) - 1)
            target_player = lateral[selection]

        if target_player:
            self._pass_to(target_player)
            return ActionResult(f"{self.player.last_name} drops puck to {target_player.last_name}")
        else:
            return ActionResult(f"{self.player.last_name} finds no open teammates")

    def pass_lateral(self):
        teammates = self.game_sim.offensive_team.get_skaters_on_ice()
        my_row = Rink.get_row(self.player.zone)
        lateral = [t for t in teammates if t != self.player and Rink.get_row(t.zone) == my_row]
        close = [t for t in teammates if abs(Rink.get_row(t.zone) - my_row) == 1]

        target_player = None
        if lateral:
            selection = self.rand.randint(0, len(lateral) - 1)
            target_player = lateral[selection]
        elif close:
            selection = self.rand.randint(0, len(close) - 1)
            target_player = close[selection]

        if target_player:
            self._pass_to(target_player)
            return ActionResult(f"{self.player.last_name} passes across to {target_player.last_name}")
        else:
            return ActionResult(f"{self.player.last_name} finds no nearby teammates")

    def pass_forward(self):
        teammates = self.game_sim.offensive_team.get_skaters_on_ice()
        my_row = Rink.get_row(self.player.zone)
        lateral = [t for t in teammates if t != self.player and Rink.get_row(t.zone) == my_row]
        up_ice = [t for t in teammates if Rink.get_row(t.zone) > my_row]
        target_player = None
        if up_ice:
            selection = self.rand.randint(0, len(up_ice) - 1)
            target_player = up_ice[selection]
        elif lateral:
            selection = self.rand.randint(0, len(lateral) - 1)
            target_player = lateral[selection]

        if target_player:
            self._pass_to(target_player)
            return ActionResult(f"{self.player.last_name} passes up to {target_player.last_name}")
        else:
            return ActionResult(f"{self.player.last_name} finds no open teammates")

    def _pass_to(self, player: Player):
        self.game_sim.puck_possessor = player
        self.game_sim.puck_zone = player.zone

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
        return ActionResult("carry_back")

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
