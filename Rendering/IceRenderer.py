from collections import defaultdict
from typing import List, Tuple
import pygame
from pygame import Surface, Color
from pygame.font import Font, SysFont
from GameSim import GameSim
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Skater import Skater
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

    player_locations = defaultdict()

    def __init__(self, game: "GameSim.GameSim", screen: Surface, zoom_factor: float):
        self.game_sim = game
        self.screen = screen
        self.render_helper = RenderingHelper(zoom_factor)
        self.font = SysFont("Impact", round(22 * zoom_factor))

    def debug_render(self):
        t = Team()
        for zone in range(1, 34):
            p = Skater(t)
            t.skaters.append(p)
            p.preferred_num = zone

            p2 = Skater(t)
            t.skaters.append(p2)
            p2.preferred_num = zone + 10

            p3 = Skater(t)
            t.skaters.append(p3)
            p3.preferred_num = zone + 20

            p.zone = Zone(zone)
            p2.zone = p.zone
            p3.zone = p.zone

            self.render_players_in_zone(p.zone, [p, p2, p3])

    def _get_player_jersey(self, player: Player):
        # TODO: This is a garbage way to determine what jersey to show
        return self.green_jersey if player.team.team_colour == "Green" else self.orange_jersey

    def render_players_in_zone(self, zone: Zone, players: List[Player]):
        centre = self.render_helper.get_centre_of_zone(zone.value)

        if len(players) == 1:
            top_lefts = [
                (centre[0] - (self.jersey_size[0] / 2), centre[1] - (self.jersey_size[1] / 2))
            ]
        elif len(players) == 2:
            top_lefts = [
                (centre[0] - self.jersey_size[0], centre[1] - (self.jersey_size[1] / 2)),
                (centre[0], centre[1] - (self.jersey_size[1] / 2)),
            ]
        elif len(players) == 3:
            top_lefts = [
                (centre[0] - (self.jersey_size[0] / 2), centre[1] - self.jersey_size[1]),
                (centre[0] - self.jersey_size[0], centre[1]),
                (centre[0], centre[1]),
            ]
        elif len(players) == 4:
            top_lefts = [
                (centre[0], centre[1]),
                (centre[0] - self.jersey_size[0], centre[1]),
                (centre[0] - self.jersey_size[0], centre[1] - self.jersey_size[1]),
                (centre[0], centre[1] - self.jersey_size[1]),
            ]
        else:
            # TODO: Not this
            raise Exception(f"Yeah.... 5 players in a zone is not supported yet. {zone}")
        for i in range(0, len(players)):
            self.render_player(players[i], self._get_player_jersey(players[i]), top_lefts[i])

    def render_current_situation(self):
        zone_contents = defaultdict(list)

        for player in self.game_sim.home_team.get_players_on_ice():
            zone_contents[player.zone].append(player)

        for player in self.game_sim.away_team.get_players_on_ice():
            zone_contents[player.zone].append(player)

        for zone in zone_contents.keys():
            self.render_players_in_zone(zone, zone_contents[zone])

        self.render_puck_location()
        return

    def render_puck_location(self):
        if self.game_sim.puck_possessor is None:
            puck_loc = self.render_helper.get_centre_of_zone(self.game_sim.puck_zone.value)
            pygame.draw.circle(self.screen, "black", puck_loc, 7)
            puck_loc = self.render_helper.get_centre_of_zone(self.game_sim.puck_zone.value)
            pygame.draw.circle(self.screen, "yellow", puck_loc, 6, 1)
        else:
            puck_loc = self.render_helper.get_centre_of_zone(self.game_sim.puck_zone.value)
            pygame.draw.circle(self.screen, "purple", puck_loc, 7)

    def render_player(self, player: Player, jersey: Surface, top_left):
        self._render_player_motion(player, top_left)

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

    def _render_player_motion(self, player: Player, new_pos: Tuple[float, float]):
        new_pos = (new_pos[0] + 10, new_pos[1] + 10)
        if player not in self.player_locations.keys():
            self.player_locations[player] = new_pos
            return
        prev = self.player_locations[player]
        if prev != new_pos:
            pygame.draw.line(self.screen, start_pos=prev, end_pos=new_pos, color=Color("Red"))
            self.player_locations[player] = new_pos
