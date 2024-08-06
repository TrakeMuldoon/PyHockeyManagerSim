from abc import ABC, abstractmethod
from GameSim import GameSim
from GameSim.Resolvers.GenericResolver import GenericResolver
from GameSim.SupportClasses.Player import Player


class OffensiveTeamActionResolver(GenericResolver):
    def __init__(self, sim: "GameSim.GameSim"):
        super().__init__(sim)

    @abstractmethod
    def resolve_action(self, action: str, player: Player) -> None:
        pass
