from abc import ABC, abstractmethod
from typing import List
from GameSim import GameSim
from GameSim.ActionResult import ActionResult
from GameSim.Resolvers.GenericResolver import GenericResolver
from GameSim.SupportClasses.Player import Player


class PossessorActionResolver(GenericResolver):
    def __init__(self, sim: "GameSim.GameSim"):
        super().__init__(sim)

    @abstractmethod
    def resolve_action(self, action: str, player: Player) -> ActionResult:
        pass
