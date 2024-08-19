from collections import defaultdict
from typing import Tuple
import pygame
from pygame import Color, Surface, transform, image
from pygame.font import Font, SysFont
from GameSim.SupportClasses.Player import Player
from Rendering.Jerseys import Jerseys
from Rendering.RenderingHelpers import RenderingHelper


class PlayerRenderer:
    font: Font

    def __init__(self, screen: Surface, zoom_factor: float):
        self.screen = screen
        self.zoom_factor = zoom_factor
        self.font = SysFont("Impact", round(22 * zoom_factor))
        self.rendering_helper = RenderingHelper(zoom_factor)

        # self.incrementor = 1

    def render_player(self, player: Player, top_left):
        self._render_player_motion(player)
        jersey_surface: Surface = Jerseys[player.team.team_colour]
        # render jersey
        self.screen.blit(jersey_surface, top_left)

        # Snippet to make the jerseys change color
        # self.incrementor += 18
        # if self.incrementor > 255:
        #     self.incrementor = 0
        # targ = Jerseys.get(self.incrementor, self.incrementor, self.incrementor)
        #
        # self.screen.blit(targ, (top_left[0] + 20, top_left[1] + 20))
        # return

        # render number
        # TODO: Render the number offsets according to the zoom_scaling
        """
            # centre the text
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

    def _render_player_motion(self, player: Player):
        if len(player.position_list) < 2:
            return
        end = len(player.position_list) - 1

        curr_coords = self.rendering_helper.get_centre_of_zone(player.position_list[end].value)
        prev_coords = self.rendering_helper.get_centre_of_zone(player.position_list[end-1].value)

        pygame.draw.line(self.screen, start_pos=prev_coords, end_pos=curr_coords, color=Color("Red"))

        if len(player.position_list) < 3:
            return

        prev_prev = self.rendering_helper.get_centre_of_zone(player.position_list[end-2].value)
        pygame.draw.line(self.screen, start_pos=prev_prev, end_pos=prev_coords, color=Color("Red"))

    def draw_gradient_line(self, color_one, color_two, start_point, end_point, segments: int = 3):
        pass
