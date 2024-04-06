class Team:
    def __init__(self):
        self.location = None
        self.team_name = None
        self.players = []
        self.goalies = []

    def print_team(self):
        print(f"{self.team_name} from {self.location}")
        print("PLAYERS")
        for player in self.players:
            print("\t", end='')
            player.print_stats()
        for goalie in self.goalies:
            print("\t", end='')
            goalie.print_stats()
