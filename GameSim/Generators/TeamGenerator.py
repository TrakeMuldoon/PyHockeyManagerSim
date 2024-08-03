from GameSim.Generators.TeamNameGenerator import TeamNameGenerator
from GameSim.SupportClasses.Goalie import Goalie
from GameSim.SupportClasses.Skater import Skater
from GameSim.SupportClasses.Team import Team


class TeamGenerator:

    @staticmethod
    def generate_random_team():
        t = Team()
        TeamNameGenerator.populate_team_information(t)
        for i in range(22):
            s = Skater(t)
            t.skaters.append(s)
        for i in range(3):
            g = Goalie(t)
            t.goalies.append(g)
        return t
