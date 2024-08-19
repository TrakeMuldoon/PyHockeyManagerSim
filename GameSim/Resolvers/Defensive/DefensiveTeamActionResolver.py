from abc import abstractmethod

from GameSim import GameSim
from GameSim.SupportClasses.Player import Player


class DefensiveTeamActionResolver:
    def __init__(self, sim: "GameSim.GameSim"):
        pass

    # TODO Rename this function to indicate it mutates and returns None
    @abstractmethod
    def resolve_action(self, action: str, player: Player) -> None:
        pass
