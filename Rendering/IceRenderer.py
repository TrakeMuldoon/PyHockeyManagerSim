from collections import defaultdict
from typing import List
import pygame
from pygame import Surface
from GameSim import GameSim
from GameSim.SupportClasses.Player import Player
from GameSim.SupportClasses.Skater import Skater
from GameSim.SupportClasses.Team import Team
from GameSim.SupportClasses.Zones import Zone
from Rendering.Jerseys import Jerseys
from Rendering.PlayerRenderer import PlayerRenderer
from Rendering.RenderingHelpers import RenderingHelper

pygame.font.init()


class IceRenderer:
    game_sim: "GameSim.GameSim"
    screen: Surface

    render_helper: RenderingHelper
    player_renderer: PlayerRenderer

    def __init__(self, game: "GameSim.GameSim", screen: Surface, zoom_factor: float):
        self.game_sim = game
        self.screen = screen
        self.render_helper = RenderingHelper(zoom_factor)
        self.player_renderer = PlayerRenderer(screen, zoom_factor)

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

    def render_players_in_zone(self, zone: Zone, players: List[Player]):
        centre = self.render_helper.get_centre_of_zone(zone.value)
        jersey_size = Jerseys.default_size()

        if len(players) == 1:
            top_lefts = [(centre[0] - (jersey_size[0] / 2), centre[1] - (jersey_size[1] / 2))]
        elif len(players) == 2:
            top_lefts = [
                (centre[0] - jersey_size[0], centre[1] - (jersey_size[1] / 2)),
                (centre[0], centre[1] - (jersey_size[1] / 2)),
            ]
        elif len(players) == 3:
            top_lefts = [
                (centre[0] - (jersey_size[0] / 2), centre[1] - jersey_size[1]),
                (centre[0] - jersey_size[0], centre[1]),
                (centre[0], centre[1]),
            ]
        elif len(players) == 4:
            top_lefts = [
                (centre[0], centre[1]),
                (centre[0] - jersey_size[0], centre[1]),
                (centre[0] - jersey_size[0], centre[1] - jersey_size[1]),
                (centre[0], centre[1] - jersey_size[1]),
            ]
        else:
            # TODO: Not this
            raise Exception(f"Yeah.... 5 players in a zone is not supported yet. {zone}")
        for i in range(0, len(players)):
            self.player_renderer.render_player(players[i], top_lefts[i])

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
