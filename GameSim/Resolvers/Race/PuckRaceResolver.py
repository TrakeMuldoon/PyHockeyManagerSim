from GameSim import GameSim


class PuckRaceResolver:
    game_sim: "GameSim.GameSim"

    def __init__(self, sim: "GameSim.GameSim"):
        game_sim = sim
        pass

    def resolve_race(self):
        print("Race! REPLACE", end="\t\t")
