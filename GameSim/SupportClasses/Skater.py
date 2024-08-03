from random import random
# from GameSim.SupportClasses.Team import Team
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Positions import Position


class Skater(Player):
    def __init__(self, team: "Team") -> None:
        super().__init__(team)
        self.speed: float = self.generate_random_NHL_stat()
        self.endurance: float = self.generate_random_NHL_stat()

        self.short_shooting: float = self.generate_random_NHL_stat()
        self.long_shooting: float = self.generate_random_NHL_stat()
        self.puck_control: float = self.generate_random_NHL_stat()
        self.passing: float = self.generate_random_NHL_stat()

        self.shot_blocking: float = self.generate_random_NHL_stat()
        self.stick_checking: float = self.generate_random_NHL_stat()

        self.position: Position = Position(int(random() * 5) + 2)

    def print_stats(self):
        name = f"{self.first_name} {self.last_name} ({str(self.position)[10:]})"
        player = f"SPD:{self.speed}\tEND:{self.endurance}"
        offence = f"WRST:{self.short_shooting}\tSLAP:{self.long_shooting}\tPC:{self.puck_control:<9}PASS:{self.passing}"
        defence = f"BLK:{self.shot_blocking}\tSCHK:{self.stick_checking}"
        print(f"{name:<40}>>\t{player}\t|\t{offence}\t|\t{defence}")

        """
        Athletic
        - Speed (to resolve races)
        - Endurance (how their stats flag over the course of the game)

        Offensive
        - Puck Control (to resolve dekes)
        - Short Shooting (Zones close to the net)
        - Long Shooting (Zones far from the net)
        - Passing

        Defensive
        - Shot Blocking (to oppose Long Shooting)
        - Stick-Checking (to oppose puck control and passing)

        """
