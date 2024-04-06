class Team:
    def __init__(self):
        self.location = None
        self.team_name = None
        self.players = []

    def print_team(self):
        print(f"{self.team_name} from {self.location}")