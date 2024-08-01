import pygame
from pygame import Surface
from pygame.font import Font, SysFont
from GameSim import GameSim
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Zones import Zone
from Rendering.RenderingHelpers import RenderingHelper

pygame.font.init()


class IceRenderer:
    game_sim: "GameSim.GameSim"
    screen: Surface

    # TODO include the jerseys in the zoom_scaling

    green_jersey = pygame.image.load("Assets/Green.png")
    green_jersey = pygame.transform.smoothscale(green_jersey, (40, 40))

    orange_jersey = pygame.image.load("Assets/OrangeJersey.png")
    orange_jersey = pygame.transform.smoothscale(orange_jersey, (40, 40))

    render_helper: RenderingHelper
    font: Font

    def __init__(self, game: "GameSim.GameSim", screen: Surface, zoom_factor: float):
        self.game_sim = game
        self.screen = screen
        self.render_helper = RenderingHelper(zoom_factor)
        self.font = SysFont("Impact", round(22 * zoom_factor))

    def debug_render(self):
        for zone in range(1,34):
            p = Player()
            p.preferred_num = zone
            p.zone = Zone(zone)
            self.render_player(p, jersey_num=1)

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
        target_location = self.render_helper.get_centre_of_zone(player.zone.value)

        # render jersey
        if jersey_num == 1:
            self.screen.blit(self.green_jersey, target_location)
        else:
            self.screen.blit(self.orange_jersey, target_location)

        # render number
        #TODO: Render the number offsets according to the zoom_scaling
        text_surface = self.font.render(str(player.preferred_num), False, (0, 0, 0))
        if player.preferred_num < 10:
            offset = target_location[0] + 15, target_location[1] + 4
        else:
            offset = target_location[0] + 9, target_location[1] + 4
        self.screen.blit(text_surface, offset)

        print(f"{player.last_name},{player.zone.value}")
