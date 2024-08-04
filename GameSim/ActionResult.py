from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Zones import Zone


class ActionResult:
    def __init__(
        self,
        new_puck_zone: Zone,
        puck_possessor: Player
    ) -> None:
        self.result_string: str = ""
        self.new_puck_zone: Zone = new_puck_zone
        self.new_puck_possessor: Player = puck_possessor
        self.possession_change: bool = False
        self.face_off: bool = False
        self.penalty: str
