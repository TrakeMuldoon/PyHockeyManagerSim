from GameSim.Player import Player


class OffensiveLine:
    def __init__(self):
        self.left_winger: Player = None  # type: ignore
        self.right_winger: Player = None  # type: ignore
        self.centre: Player = None  # type: ignore
        self.extra_player: Player = None  # type: ignore

        self.line_average_player: Player = None  # type: ignore


class DefensiveLine:
    def __init__(self):
        self.left_defence: Player = None  # type: ignore
        self.right_defence: Player = None  # type: ignore

        self.line_average_player: Player = None  # type: ignore
