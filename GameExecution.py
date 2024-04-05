from GameSim.Player import Player
from GameSim.Goalie import Goalie

if __name__ == '__main__':
    for i in range(20):
        p = Player()
        p.print_stats()

    for i in range(5):
        g = Goalie()
        g.print_stats()