# Example file showing a basic pygame "game loop"
import pygame
from GameSim.GameSim import GameSim
from GameSim.Generators.TeamGenerator import TeamGenerator
from Rendering.Button import Button
from Rendering.IceRenderer import IceRenderer
from Rendering.Jerseys import Jerseys

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
game_over = False
game_event_generator = game.yield_simulate_game()

run_button = Button((50, 200, 25), 550, 10, 130, 75, 'Run')
event_button = Button((70, 160, 185), 550, 100, 130, 75, 'One')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(image, dest=(0, 0))
    run_button.draw(screen)
    event_button.draw(screen)

    """
        GAME STUFF
    """
    # game_renderer.debug_render()
    game_renderer.render_current_situation()
    result_string = "Final Score"
    if not game_over:
        # result_string = game.simulate_next_event()
        result_string = next(game_event_generator)

    if result_string.startswith("Final Score"):
        game_over = True
    print(result_string)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
