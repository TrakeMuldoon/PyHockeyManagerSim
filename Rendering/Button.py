import pygame
from pygame import Surface, Rect
from pygame.font import Font

pygame.font.init()


class Button:
    font = Font(None, 35)

    def __init__(self, color, x, y, width, height, text):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_ren = self.font.render(text, True, (255, 255, 255))
        self.rect = Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen: Surface):
        button = pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        screen.blit(self.text_ren, (button.x + 5, button.y + 5))

    def get_rect(self) -> Rect:
        return self.rect
