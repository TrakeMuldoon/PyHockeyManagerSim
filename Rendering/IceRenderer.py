import pygame
from pygame import Surface
from GameSim import GameSim
from GameSim.SupportClasses.Player import Player
from Rendering.RenderingHelpers import ZoneToPixelLocation


class IceRenderer:
    game_sim: "GameSim.GameSim"
    screen: Surface

    green_jersey = pygame.image.load("Assets/Green.png")
    green_jersey = pygame.transform.smoothscale(green_jersey, (40, 40))

    orange_jersey = pygame.image.load("Assets/OrangeJersey.png")
    orange_jersey = pygame.transform.smoothscale(orange_jersey, (40, 40))

    def __init__(self, game: "GameSim.GameSim", screen: Surface):
        self.game_sim = game
        self.screen = screen

    def render_current_situation(self):
        for player in self.game_sim.home_team.get_active_players():
            self.render_player(player, 1)
        self.render_player(self.game_sim.home_team.goalie, 1)
        print("---")
        for player in self.game_sim.away_team.get_active_players():
            self.render_player(player, 2)
        self.render_player(self.game_sim.away_team.goalie, 2)
        print("---------------------")

    def render_player(self, player: Player, jersey_num: int):
        target_location = ZoneToPixelLocation[player.zone.value]
        print(f"{player.last_name},{player.zone.value}")
        if jersey_num == 1:
            self.screen.blit(self.green_jersey, target_location)
        else:
            self.screen.blit(self.orange_jersey, target_location)
