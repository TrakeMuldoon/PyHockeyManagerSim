import math
from typing import List

import pygame
from pygame import Color, Surface
from pygame.font import Font, SysFont
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Zones import Zone
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
        # self._render_player_motion(player)
        self._render_player_motion_bezier_double(player, draw_dots=False)
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

    def _render_player_motion_bezier_double(
        self,
        player: Player,
        draw_dots: bool = True,
        draw_line: bool = True,
        num_segments: int = 10,
        start_colour: Color = Color(255, 255, 255),
        end_colour: Color = Color(0, 0, 0),
    ):
        if len(player.position_list) < 3:
            return

        point_set = self.generate_point_set(player.position_list)

        # Debug Draw Circles on the Points
        for p in point_set:
            pygame.draw.circle(self.screen, (0, 110, 0), p, 5)

        # Get Bezier Points
        bez_points = self.generate_bezier_points(point_set, num_segments)

        t = 0.0
        sc = start_colour
        ec = end_colour
        colour_delta = ((ec.r - sc.r), (ec.g - sc.g), (ec.b - sc.b))

        current_colour = sc
        last_point = None
        for i, point in enumerate(bez_points):
            if draw_dots:
                pygame.draw.rect(self.screen, start_colour, (point[0], point[1], 3, 3))
            if draw_line:
                mod = i / (len(bez_points) - 1)
                current_colour = (
                    start_colour.r + (colour_delta[0] * mod),
                    start_colour.g + (colour_delta[1] * mod),
                    start_colour.b + (colour_delta[2] * mod),
                )
                if last_point is not None:
                    pygame.draw.line(self.screen, current_colour, last_point, point, 1)
                last_point = point
        pass

    def generate_point_set(self, loc_history: List[Zone], target_points: int = 4):
        # simple version with no extra points added
        zone_centre = self.rendering_helper.get_centre_of_zone
        point_list = [zone_centre(z.value) for z in loc_history[-target_points:]]
        return point_list

    def generate_bezier_points(self, point_list, num_iterations):
        # https://pomax.github.io/bezierinfo/
        num_points = len(point_list)
        if num_points > 4 or num_points < 3:
            raise Exception("BEZIER points error", num_points)

        points = []
        for i in range(0, num_iterations):
            t = i / num_iterations
            point = None
            if num_points == 3:
                point = self.bez_3(t, point_list, [1, 1, 1])
                # point = self.bez_3(t, point_list, [0.15, 1.90, 0.15])
            if num_points == 4:
                point = self.bez_4(t, point_list, [1, 1, 1, 1])
                # point = self.bez_4(t, point_list, [0.20, 1.85, 1.85, 0.20])
            points.append(point)

        return points

    def bez_3(self, t, point_set, weight_set):
        t_sq = t * t
        mt = 1 - t
        mt_sq = mt * mt

        fx = [point_set[0][0] * mt_sq,
              2 * point_set[1][0] * mt * t,
              point_set[2][0] * t_sq]
        fy = [point_set[0][1] * mt_sq,
              2 * point_set[1][1] * mt * t,
              point_set[2][1] * t_sq]

        basis_x = fx[0] + fx[1] + fx[2]
        basis_y = fy[0] + fy[1] + fy[2]

        weighted_value_x = (fx[0] * weight_set[0] + fx[1] * weight_set[1] + fx[2] * weight_set[2]) / basis_x
        weighted_value_y = (fy[0] * weight_set[0] + fy[1] * weight_set[1] + fy[2] * weight_set[2]) / basis_y
        point = (weighted_value_x, weighted_value_y)
        return point

#     function
#     RationalBezier(2, t, w[], r[]):
#     t2 = t * t
#     mt = 1 - t
#     mt2 = mt * mt
#     f = [
#         r[0] * mt2,
#         2 * r[1] * mt * t,
#         r[2] * t2
#     ]
#     basis = f[0] + f[1] + f[2]
#     return (f[0] * w[0] + f[1] * w[1] + f[2] * w[2]) / basis
#
#
# function
# RationalBezier(3, t, w[], r[]):
# t2 = t * t
# t3 = t2 * t
# mt = 1 - t
# mt2 = mt * mt
# mt3 = mt2 * mt
# f = [
#     r[0] * mt3,
#     3 * r[1] * mt2 * t,
#     3 * r[2] * mt * t2,
#     r[3] * t3
# ]
# basis = f[0] + f[1] + f[2] + f[3]
# return (f[0] * w[0] + f[1] * w[1] + f[2] * w[2] + f[3] * w[3]) / basis

    def bez_4(self, t, point_set, weight_set):
        t_sq = t * t
        t_cu = t_sq * t
        mt = 1 - t
        mt_sq = mt * mt
        mt_cu = mt_sq * mt

        fx = [point_set[0][0] * mt_cu,
              3 * point_set[1][0] * mt_sq * t,
              3 * point_set[2][0] * mt * t_sq,
              point_set[3][0] * t_cu]
        fy = [point_set[0][1] * mt_cu,
              3 * point_set[1][1] * mt_sq * t,
              3 * point_set[2][1] * mt * t_sq,
              point_set[3][1] * t_cu]

        basis_x = fx[0] + fx[1] + fx[2] + fx[3]
        basis_y = fy[0] + fy[1] + fy[2] + fy[3]

        weighted_value_x = (fx[0] * weight_set[0]
                            + fx[1] * weight_set[1]
                            + fx[2] * weight_set[2]
                            + fx[3] * weight_set[3]) / basis_x
        weighted_value_y = (fy[0] * weight_set[0]
                            + fy[1] * weight_set[1]
                            + fy[2] * weight_set[2]
                            + fy[3] * weight_set[3]) / basis_y
        point = (weighted_value_x, weighted_value_y)
        return point

    def _modify_colour(self, current: Color, increment):
        r = math.floor(current.r + increment[0])
        g = math.floor(current.g + increment[1])
        b = math.floor(current.b + increment[2])
        updated = Color(r, g, b)
        return updated

    def _render_player_motion(self, player: Player):
        if len(player.position_list) < 2:
            return
        end = len(player.position_list) - 1

        curr_coords = self.rendering_helper.get_centre_of_zone(player.position_list[end].value)
        prev_coords = self.rendering_helper.get_centre_of_zone(player.position_list[end - 1].value)

        pygame.draw.line(
            self.screen, start_pos=prev_coords, end_pos=curr_coords, color=Color("Red")
        )

        if len(player.position_list) < 3:
            return

        prev_prev = self.rendering_helper.get_centre_of_zone(player.position_list[end - 2].value)
        pygame.draw.line(self.screen, start_pos=prev_prev, end_pos=prev_coords, color=Color("Red"))

    def draw_gradient_line(self, color_one, color_two, start_point, end_point, segments: int = 3):
        pass
