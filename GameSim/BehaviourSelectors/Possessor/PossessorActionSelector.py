from GameSim import GameSim


class PossessorActionSelector:
    game_sim: "GameSim.GameSim"

    def __init__(self, sim: "GameSim.GameSim"):
        self.game_sim = sim
        pass
