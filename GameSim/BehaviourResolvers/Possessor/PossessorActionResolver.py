from abc import ABC, abstractmethod
from typing import List
from GameSim import GameSim
from GameSim.ActionResult import ActionResult
from GameSim.BehaviourResolvers.GenericResolver import GenericResolver
from GameSim.SupportClasses.Player import Player


class PossessorActionResolver(GenericResolver):
    def __init__(self, sim: "GameSim.GameSim"):
        super().__init__(sim)

    # TODO Rename this function to indicate it does not mutate, and returns an Action Result
    @abstractmethod
    def resolve_action(self, action: str, player: Player) -> ActionResult:
        pass
