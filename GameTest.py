# Example file showing a basic pygame "game loop"
import math
from itertools import cycle
from typing import List
import pygame
from GameSim.GameSim import GameSim
from GameSim.Generators.TeamGenerator import TeamGenerator
from Rendering.Button import Button
from Rendering.IceRenderer import IceRenderer
from Rendering.threshold import Threshold


def find_quit(events):
    quitting = tuple(filter(lambda event: event.type == pygame.QUIT, events))
    return not bool(quitting)


def is_button_up(events):
    button_up = tuple(filter(lambda event: event.type == pygame.MOUSEBUTTONUP, events))
    return bool(button_up)


def find_button_press(buttons: List[Button]) -> Button | None:
    pos = pygame.mouse.get_pos()
    for button in buttons:
        if button.get_rect().collidepoint(pos):
            return button
    return None


def draw_looper(screen, value):
    loop_len = 20
    pygame.draw.rect(screen, "black", (799 - loop_len + value, 0, 2, 10), 0)
    value += 1
    return value if value < loop_len else 0


def main():
    pygame.init()

    # # pygame setup
    display_size = 800, 1000
    screen = pygame.display.set_mode(display_size)
    clock = pygame.time.Clock()
    running = True

    # Game Set Up
    # TODO: Obviously teams should not be set up this way
    home_team = TeamGenerator.generate_random_team()
    home_team.team_colour = "Orange"
    home_team.team_brand_colour = (255, 180, 25)
    away_team = TeamGenerator.generate_random_team()
    away_team.team_colour = "Green"
    away_team.team_brand_colour = (20, 255, 20)

    game = GameSim(home_team, away_team)
    game.set_up_for_period()

    # Simulator Set Up
    game_event_generator = game.yield_simulate_game()

    # UI SET UP
    rink_image = pygame.image.load("Assets/RinkNoLines.png")
    rink_image = pygame.transform.smoothscale(rink_image, (500, 1000))

    game_over = False
    sim_run = True
    next_step = False

    time_button_dims = (40, 80)
    buttons = [
        Button((0, 0, 255, 10), (780, 1), (20, 10), "FPS", ""),
        Button((255, 100, 100), (520, 100), time_button_dims, "OneStep", "1", "Black"),
        Button((200, 255, 0), (570, 100), time_button_dims, "SlowSpeed", "Slow", "Black"),
        Button((0, 255, 0), (620, 100), time_button_dims, "RegularSpeed", "Run", "Black"),
        Button((0, 255, 150), (670, 100), time_button_dims, "FastSpeed", "Fast", "Black"),
    ]

    game_renderer = IceRenderer(game, screen, 1.0)

    draw_cycle: cycle = cycle((10, 20, 60, 100))
    draw_timer = Threshold(60)
    game_timer = Threshold(60)
    previous_ticks = pygame.time.get_ticks()
    elapsed = 0
    draw_loop_int = 0
    while running:
        events = tuple(pygame.event.get())
        running = find_quit(events)

        if is_button_up(events):
            pressed_button = find_button_press(buttons)
            if pressed_button:
                match pressed_button.name:
                    case "FPS":
                        draw_timer.threshold = next(draw_cycle)
                    case "OneStep":
                        sim_run = False
                        next_step = True
                    case "SlowSpeed":
                        sim_run = True
                        game_timer.threshold = 1000
                    case "RegularSpeed":
                        sim_run = True
                        game_timer.threshold = 300
                    case "FastSpeed":
                        sim_run = True
                        game_timer.threshold = 30

        if game_timer.is_threshold_exceeded(elapsed):
            if not game_over and (sim_run or next_step):
                result_string = next(game_event_generator)
                next_step = False

                # Hack... yes... I agree.
                if result_string.startswith("Final Score"):
                    game_over = True
                print(result_string)

        if draw_timer.is_threshold_exceeded(elapsed):
            #     """ DRAW STEP """
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")
            screen.blit(rink_image, dest=(0, 0))
            for button in buttons:
                button.draw(screen)
            draw_loop_int = draw_looper(screen, draw_loop_int)
            game_renderer.render_current_situation()
            pygame.display.flip()

        # Set Dynamic Caption?
        # pygame.display.set_caption(f"FPS: {clock.get_fps():.2f}{' ' * 10}Animation FPS: {current_frame_rate}")

        # Finish up timing related things
        elapsed = pygame.time.get_ticks() - previous_ticks
        previous_ticks = elapsed + previous_ticks
        clock.tick(500)  # limits tick fidelity to 500
    pygame.quit()


if __name__ == "__main__":
    main()
