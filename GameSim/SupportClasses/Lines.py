from GameSim.SupportClasses.Skater import Skater


class OffensiveLine:
    def __init__(self):
        self.left_winger: Skater = None  # type: ignore
        self.right_winger: Skater = None  # type: ignore
        self.centre: Skater = None  # type: ignore
        self.extra_skater: Skater = None  # type: ignore

        self.line_average_player: Skater = None  # type: ignore

    def get_skaters(self):
        potential_skaters = [self.left_winger, self.right_winger, self.centre, self.extra_skater]
        return [ps for ps in potential_skaters if ps]


class DefensiveLine:
    def __init__(self):
        self.left_defence: Skater = None  # type: ignore
        self.right_defence: Skater = None  # type: ignore

        self.line_average_player: Skater = None  # type: ignore

    def get_skaters(self):
        potential_skaters = [self.left_defence, self.right_defence]
        return [ps for ps in potential_skaters if ps]
