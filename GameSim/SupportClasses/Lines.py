from GameSim.SupportClasses.Player import Player


class OffensiveLine:
    def __init__(self):
        self.left_winger: Player = None  # type: ignore
        self.right_winger: Player = None  # type: ignore
        self.centre: Player = None  # type: ignore
        self.extra_player: Player = None  # type: ignore

        self.line_average_player: Player = None  # type: ignore

    def get_players(self):
        potential_players = [self.left_winger, self.right_winger, self.centre, self.extra_player]
        return [p for p in potential_players if p]


class DefensiveLine:
    def __init__(self):
        self.left_defence: Player = None  # type: ignore
        self.right_defence: Player = None  # type: ignore

        self.line_average_player: Player = None  # type: ignore

    def get_players(self):
        potential_players = [self.left_defence, self.right_defence]
        return [p for p in potential_players if p]
