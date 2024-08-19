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

# Game Set Up
# TODO: Obviously teams should not be set up this way
home_team = TeamGenerator.generate_random_team()
home_team.team_colour = "Orange"
away_team = TeamGenerator.generate_random_team()
away_team.team_colour = "Green"

game = GameSim(home_team, away_team)
game.set_up_for_period()

# Simulator Set Up
game_event_generator = game.yield_simulate_game()

# UI SET UP
rink_image = pygame.image.load("Assets/RinkNoLines.png")
rink_image = pygame.transform.smoothscale(rink_image, (500, 1000))

run_button = Button((50, 200, 25), 550, 10, 130, 75, "Run")
event_button = Button((70, 160, 185), 550, 100, 130, 75, "One")

game_renderer = IceRenderer(game, screen, 1.0)

game_over = False
sim_run = True
next_step = False

while running:
    # POLL FOR EVENTS
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if run_button.get_rect().collidepoint(pos):
                sim_run = not sim_run
            if event_button.get_rect().collidepoint(pos):
                sim_run = False
                next_step = True

    """ GAME STEP """
    result_string = "Final Score"
    if not game_over and (sim_run or next_step):
        # result_string = game.simulate_next_event()
        result_string = next(game_event_generator)
        next_step = False

        if result_string.startswith("Final Score"):
            game_over = True
        print(result_string)

    """ DRAW STEP """
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(rink_image, dest=(0, 0))
    run_button.draw(screen)
    event_button.draw(screen)
    # game_renderer.debug_render()
    game_renderer.render_current_situation()

    # flip() the display to put your work on screen
    pygame.display.flip()


    clock.tick(60)  # limits FPS to 60

pygame.quit()
