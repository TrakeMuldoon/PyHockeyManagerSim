from abc import ABC, abstractmethod
from GameSim import GameSim
from GameSim.BehaviourResolvers.GenericResolver import GenericResolver
from GameSim.SupportClasses.Player import Player


class OffensiveTeamActionResolver(GenericResolver):
    def __init__(self, sim: "GameSim.GameSim"):
        super().__init__(sim)

    # TODO Rename this function to indicate it mutates and returns None
    @abstractmethod
    def resolve_action(self, action: str, player: Player) -> None:
        pass
