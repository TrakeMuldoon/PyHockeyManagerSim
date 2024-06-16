from GameSim.Generators.TeamNameGenerator import TeamNameGenerator
from GameSim.SupportClasses.Goalie import Goalie
from GameSim.SupportClasses.Player import Player
from GameSim.Team import Team


class TeamGenerator:
    # _generator = _inner_generator()

    @staticmethod
    def generate_random_team():
        t = Team()
        TeamNameGenerator.populate_team_information(t)
        for i in range(22):
            p = Player()
            t.players.append(p)
        for i in range(3):
            g = Goalie()
            t.goalies.append(g)
        return t
