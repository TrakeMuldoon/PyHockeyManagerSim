import random
from itertools import cycle

import pygame


def find_quit(events):
    quitting = tuple(filter(lambda event: event.type == pygame.QUIT, events))
    return not bool(quitting)


def should_change(events, frame_rates, current_frame_rate):
    # Press any key to change animation rate
    change = tuple(filter(lambda event: event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN], events))
    return next(frame_rates) if change else current_frame_rate


def frame_rate_independence(elapsed_time, delta_time, current_frame_rate, color):
    if elapsed_time >= 1 / current_frame_rate:
        elapsed_time = 0
        color = random.sample(range(256), 4)
    elapsed_time += delta_time

    return elapsed_time, color


def main():
    pygame.init()

    display_size = 500, 500
    display = pygame.display.set_mode(display_size)

    player = pygame.Rect((150, 150), (150, 150))
    color = random.sample(range(256), 4)
    elapsed_time = 0

    frame_rates = cycle((1, 10, 30, 60))
    current_frame_rate = next(frame_rates)
    clock = pygame.time.Clock()
    running = True
    delta_time = 0

    while running:
        events = tuple(pygame.event.get())
        running = find_quit(events)
        current_frame_rate = should_change(events, frame_rates, current_frame_rate)
        elapsed_time, color = frame_rate_independence(elapsed_time, delta_time, current_frame_rate, color)

        display.fill("black")
        pygame.draw.rect(display, color, player)
        pygame.display.flip()
        delta_time = clock.tick() * 0.001
        pygame.display.set_caption(f"FPS: {clock.get_fps():.2f}{' ' * 10}Animation FPS: {current_frame_rate}")


if __name__ == "__main__":
    main()
