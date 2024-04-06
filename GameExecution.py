from GameSim.Player import Player
from GameSim.Goalie import Goalie
from GameSim.Team import Team
from GameSim.TeamNameGenerator import TeamNameGenerator

if __name__ == '__main__':
    for i in range(20):
        p = Player()
        p.print_stats()

    for i in range(5):
        g = Goalie()
        g.print_stats()

    for i in range(5):
        t = Team()
        TeamNameGenerator.populate_team_information(t)
        t.print_team()
