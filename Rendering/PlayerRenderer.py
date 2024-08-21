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
        num_segments: int = 15,
        start_colour: Color = Color(245, 245, 245),
        end_colour: Color = Color(50, 50, 50),
    ):
        if len(player.position_list) < 3:
            return

        point_set = self.generate_point_set(player.position_list)

        # Debug Draw Circles on the Points
        # for p in point_set:
        #     pygame.draw.circle(self.screen, (0, 110, 0), p, 5)

        # Get Bezier Points
        bez_points = self.generate_bezier_points(point_set, num_segments)

        sc = start_colour
        ec = end_colour
        colour_delta = ((ec.r - sc.r), (ec.g - sc.g), (ec.b - sc.b))

        current_colour = sc
        last_point = None
        for i, point in enumerate(bez_points):
            if draw_dots:
                pygame.draw.rect(self.screen, current_colour, (point[0], point[1], 3, 3))
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
                point = self.bez_3(t, point_list, [0.4, 1.6, 0.4])
            if num_points == 4:
                point = self.bez_4(t, point_list, [0.4, 1.6, 1.6, 0.4])
            points.append(point)

        return points

    def bez_3(self, t, point_set, weight_set):
        t_sq = t * t
        mt = 1 - t
        mt_sq = mt * mt

        w = [weight_set[0] * mt_sq,
             2 * weight_set[1] * mt * t,
             weight_set[2] * t_sq
            ]

        basis = w[0] + w[1] + w[2]

        weighted_value_x = (w[0] * point_set[0][0] + w[1] * point_set[1][0] + w[2] * point_set[2][0]) / basis
        weighted_value_y = (w[0] * point_set[0][1] + w[1] * point_set[1][1] + w[2] * point_set[2][1]) / basis
        point = (weighted_value_x, weighted_value_y)
        return point


    def bez_4(self, t, point_set, weight_set):
        t_sq = t * t
        t_cu = t_sq * t
        mt = 1 - t
        mt_sq = mt * mt
        mt_cu = mt_sq * mt

        w = [
            weight_set[0] * mt_cu,
            3 * weight_set[1] * mt_sq * t,
            3 * weight_set[2] * mt * t_sq,
            weight_set[3] * t_cu
        ]

        basis = w[0] + w[1] + w[2] + w[3]

        ps = point_set
        weighted_value_x = (w[0] * ps[0][0] + w[1] * ps[1][0] + w[2] * ps[2][0] + w[3] * ps[3][0]) / basis
        weighted_value_y = ((w[0] * ps[0][1] + w[1] * ps[1][1] + w[2] * ps[2][1] + w[3] * ps[3][1]) / basis)
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
