from collections import defaultdict
import pygame
from pygame import Surface, image, transform


class Jerseys:
    # TODO include the jerseys in the zoom_scaling
    jersey_size = (40, 40)

    # TODO Remove this
    Orange = image.load("Assets/OrangeJersey.png")
    Orange = transform.smoothscale(Orange, size=jersey_size)

    # TODO Remove this
    Green = image.load("Assets/Green.png")
    Green = transform.smoothscale(Green, size=jersey_size)

    _local_dict: defaultdict = defaultdict()
    template = image.load("Assets/JerseyTemplate.png")
    template = transform.smoothscale(template, jersey_size)

    def __class_getitem__(cls, item) -> Surface:
        return Jerseys.__dict__[item]

    @staticmethod
    def default_size():
        return Jerseys.jersey_size

    # TODO Import this into _cls_item_
    @classmethod
    def get(cls, r: int, g: int, b: int):
        trupple = (r, g, b)

        if trupple in cls._local_dict:
            print("found")
            return cls._local_dict[trupple]

        if r > 255 or g > 255 or b > 255:
            raise Exception("255 is the highest value for a primary in RGB")

        print("new")
        cls._local_dict[trupple] = cls._generate_jersey(trupple)

        return cls._local_dict[trupple]

    @classmethod
    def _generate_jersey(cls, color):
        coloured_image = Surface(cls.template.get_size())
        coloured_image.fill(color)

        final_image = cls.template.copy()
        final_image.blit(coloured_image, (0, 0), special_flags=pygame.BLEND_MULT)
        return final_image
