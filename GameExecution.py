from GameSim.Player import Player
from GameSim.Goalie import Goalie
from GameSim.Team import Team
from GameSim.TeamNameGenerator import TeamNameGenerator

if __name__ == '__main__':
    for i in range(5):
        t = Team()
        TeamNameGenerator.populate_team_information(t)
        for i in range(22):
            p = Player()
            t.players.append(p)
        for i in range(3):
            g = Goalie()
            t.goalies.append(g)
        t.print_team()
        print()
