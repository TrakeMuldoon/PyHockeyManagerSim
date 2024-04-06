from GameSim.Generators.TeamGenerator import TeamGenerator

if __name__ == '__main__':
    for i in range(5):
        t = TeamGenerator.generate_random_team()
        t.print_team()
        print()
