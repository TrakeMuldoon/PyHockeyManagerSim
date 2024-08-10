from pygame import Surface, image, transform


class Jerseys:
    # TODO include the jerseys in the zoom_scaling
    jersey_size = (40, 40)

    Orange = image.load("Assets/OrangeJersey.png")
    Orange = transform.smoothscale(Orange, size=jersey_size)

    Green = image.load("Assets/Green.png")
    Green = transform.smoothscale(Green, size=jersey_size)

    def __class_getitem__(cls, item) -> Surface:
        return Jerseys.__dict__[item]

    @staticmethod
    def default_size():
        return Jerseys.jersey_size
