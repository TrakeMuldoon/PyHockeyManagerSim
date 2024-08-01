from GameSim import GameSim
from GameSim.Resolvers.Possessor.PossessorActionResolver import PossessorActionResolver


class DummyResolver(PossessorActionResolver):
    def __init__(self, sim: "GameSim.GameSim"):
        super().__init__(sim)

    def forward_pass(self):
        print("forward pass")
        pass

    def lateral_pass(self):
        print("lateral pass")
        pass

    def backward_pass(self):
        print("backward pass")
        pass

    def carry(self):
        print("carry")
        pass

    def clear(self):
        print("clear")
        pass

    def dump(self):
        print("dump")
        pass

    def outside_pass(self):
        print("outside pass")
        pass

    def central_pass(self):
        print("central pass")
        pass

    def shoot(self):
        print("shoot")
        pass
