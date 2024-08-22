import pygame
from pygame import Color, Rect, Surface
from pygame.font import Font

pygame.font.init()


class Button:
    font = Font(None, 35)

    def __init__(
        self, color, xy, dimensions, name, text, text_color: Color = Color("White"), on_click=None
    ):
        self.base_color = color
        self.color = color
        self.x = xy[0]
        self.y = xy[1]
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.name = name
        self.text = text
        self.text_ren = self.font.render(text, True, text_color)
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.on_click = on_click

    def draw(self, screen: Surface):
        button = pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        screen.blit(self.text_ren, (button.x + 5, button.y + 20))

    def get_rect(self) -> Rect:
        return self.rect
