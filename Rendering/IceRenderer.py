from collections import defaultdict
from typing import List
import pygame
from pygame import Surface
from pygame.font import Font, SysFont
from GameSim import GameSim
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Team import Team
from GameSim.SupportClasses.Zones import Zone
from Rendering.RenderingHelpers import RenderingHelper

pygame.font.init()


class IceRenderer:
    game_sim: "GameSim.GameSim"
    screen: Surface

    # TODO include the jerseys in the zoom_scaling
    jersey_size = (40, 40)

    green_jersey = pygame.image.load("Assets/Green.png")
    green_jersey = pygame.transform.smoothscale(green_jersey, size=jersey_size)

    orange_jersey = pygame.image.load("Assets/OrangeJersey.png")
    orange_jersey = pygame.transform.smoothscale(orange_jersey, size=jersey_size)

    render_helper: RenderingHelper
    font: Font

    def __init__(self, game: "GameSim.GameSim", screen: Surface, zoom_factor: float):
        self.game_sim = game
        self.screen = screen
        self.render_helper = RenderingHelper(zoom_factor)
        self.font = SysFont("Impact", round(22 * zoom_factor))

    def debug_render(self):
        t = Team()
        for zone in range(1, 34):
            p = Player(t)
            t.players.append(p)
            p.preferred_num = zone

            p2 = Player(t)
            t.players.append(p2)
            p2.preferred_num = zone + 10

            p3 = Player(t)
            t.players.append(p3)
            p3.preferred_num = zone + 20

            p.zone = Zone(zone)
            p2.zone = p.zone
            p3.zone = p.zone

            self.render_players_in_zone(p.zone, [p, p2, p3])

    def render_players_in_zone(self, zone: Zone, players: List[Player]):
        centre = self.render_helper.get_centre_of_zone(zone.value)
        # players_width = self.jersey_size[0] * len(players)

        if len(players) == 1:
            top_left = (
                centre[0] - (self.jersey_size[0] / 2),
                centre[1] - (self.jersey_size[1] / 2),
            )
            self.render_player(players[0], self.green_jersey, top_left)
            return
        if len(players) == 2:
            tl_1 = (centre[0] - self.jersey_size[0], centre[1] - (self.jersey_size[1] / 2))
            tl_2 = (centre[0], centre[1] - (self.jersey_size[1] / 2))

            self.render_player(players[0], self.green_jersey, tl_1)
            self.render_player(players[1], self.green_jersey, tl_2)
            return
        if len(players) == 3:
            tl_1 = (centre[0] - (self.jersey_size[0] / 2), centre[1] - self.jersey_size[1])
            tl_2 = (centre[0] - self.jersey_size[0], centre[1])
            tl_3 = (centre[0], centre[1])
            self.render_player(players[0], self.green_jersey, tl_1)
            self.render_player(players[1], self.green_jersey, tl_2)
            self.render_player(players[2], self.green_jersey, tl_3)

    def render_current_situation(self):
        zone_contents = defaultdict(List)
        for player in self.game_sim.home_team.get_active_players():
            zone_contents[player.zone.value].append(player)
        for player in self.game_sim.away_team.get_active_players():
            zone_contents[player.zone.value].append(player)
        print(zone_contents)
        return
        # for player in self.game_sim.home_team.get_active_players():
        #    self.render_player(player, 1)
        # self.render_player(self.game_sim.home_team.goalie, 1)
        # print("---")
        # for player in self.game_sim.away_team.get_active_players():
        #    self.render_player(player, 2)
        # self.render_player(self.game_sim.away_team.goalie, 2)
        # print("---------------------")

    def render_player(self, player: Player, jersey: Surface, top_left):
        # render jersey
        self.screen.blit(jersey, top_left)

        # render number
        # TODO: Render the number offsets according to the zoom_scaling
        """
            # draw text
            font = pygame.font.Font(None, 25)
            text = font.render("You win!", True, BLACK)
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            screen.blit(text, text_rect)
        """
        text_surface = self.font.render(str(player.preferred_num), False, (0, 0, 0))
        if player.preferred_num < 10:
            offset = top_left[0] + 15, top_left[1] + 4
        else:
            offset = top_left[0] + 9, top_left[1] + 4
        self.screen.blit(text_surface, offset)

        print(f"{player.last_name},{player.zone.value}")
