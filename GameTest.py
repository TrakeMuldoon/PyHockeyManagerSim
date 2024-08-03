# Example file showing a basic pygame "game loop"
import pygame
from GameSim.GameSim import GameSim
from GameSim.Generators.TeamGenerator import TeamGenerator
from Rendering.IceRenderer import IceRenderer

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 1000))
clock = pygame.time.Clock()
running = True

image = pygame.image.load("Assets/RinkNoLines.png")
image = pygame.transform.smoothscale(image, (500, 1000))

# TODO: Obviously teams should not be set up this way
home_team = TeamGenerator.generate_random_team()
home_team.team_colour = "Orange"
away_team = TeamGenerator.generate_random_team()
away_team.team_colour = "Green"

game = GameSim(home_team, away_team)
game_renderer = IceRenderer(game, screen, 1.0)

game.set_up_for_period()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(image, dest=(0, 0))

    """
        GAME STUFF
    """
    # game_renderer.debug_render()
    game_renderer.render_current_situation()
    game.simulate_next_event()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
