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

    def _render_player_motion_bezier_double(self, player: Player
                                            , draw_dots: Boolean = True
                                            , draw_line: Boolean = True
                                            , num_lines: int = 5):
        if len(player.position_list) < 2:
            return
        end_pos = len(player.position_list) - 1

        p0 = player.position_list[end_pos-2]
        p1 = player.position_list[end_pos-1]
        p2 = player.position_list[end_pos]
        lastPoint = None

        for p in [p0, p1, p2]:
            pygame.draw.circle(screen, (150, 150, 150), p, 5)
        for t in np.arange(0, 1, 1.1/num_lines):
            px = p0[0]*(1-t)**2 + 2*(1-t)*t*p1[0] + p2[0]*t**2
            py = p0[1]*(1-t)**2 + 2*(1-t)*t*p1[1] + p2[1]*t**2
            bez_point = (px, py)
            if(draw_dots)
                pygame.draw.rect(screen, (255, 255, 0), (px, py, 3, 3))
            if(draw_line)
                if lastPoint is not None:
                    pygame.draw.line(screen, (255, 255, 0), lastPoint, point, 1)
                lastPoint = point 
            

    
    def _render_player_motion(self, player: Player):
        if len(player.position_list) < 2:
            return
        end = len(player.position_list) - 1

        curr_coords = self.rendering_helper.get_centre_of_zone(player.position_list[end].value)
        prev_coords = self.rendering_helper.get_centre_of_zone(player.position_list[end-1].value)

        pygame.draw.line(self.screen, start_pos=prev_coords, end_pos=curr_coords, color=Color("Red"))

    # def _render_player_motion(self, player: Player, new_pos: Tuple[float, float]):
    #     new_pos = (new_pos[0] + 10, new_pos[1] + 10)
    #     if player not in self.player_locations.keys():
    #         self.player_locations[player] = new_pos
    #         return
    #     prev = self.player_locations[player]
    #     if prev != new_pos:
    #         pygame.draw.line(self.screen, start_pos=prev, end_pos=new_pos, color=Color("Red"))
    #         self.player_locations[player] = new_pos
