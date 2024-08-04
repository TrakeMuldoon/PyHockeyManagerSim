from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Zones import Zone


class ActionResult:
    def __init__(
        self,
        new_puck_zone: Zone,
        puck_possessor: Player,
    ) -> None:
        self.result_string: str = ""
        self.new_puck_zone: Zone = None
        self.new_puck_possessor: Player = None
        self.possession_change: bool = False
        self.face_off: bool = False
        self.penalty: str
