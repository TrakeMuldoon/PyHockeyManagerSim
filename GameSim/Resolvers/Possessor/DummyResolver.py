from GameSim import GameSim
from GameSim.Resolvers.Possessor.PossessorActionResolver import PossessorActionResolver


class DummyResolver(PossessorActionResolver):
    def __init__(self, sim: "GameSim.GameSim"):
        super().__init__(sim)

    def forward_pass(self):
        pass

    def lateral_pass(self):
        pass

    def backward_pass(self):
        pass

    def carry(self):
        pass

    def clear(self):
        pass

    def dump(self):
        pass

    def outside_pass(self):
        pass

    def central_pass(self):
        pass

    def shoot(self):
        pass
