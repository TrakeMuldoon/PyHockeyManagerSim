class RenderingHelper:
    zoom_factor: float = 1.0

    def __init__(self, zoom_factor: float):
        self.zoom_factor = zoom_factor

    def get_centre_of_zone(self, zone_num: int):
        coord = self.ZoneToPixelLocation[zone_num]
        return coord[0] * self.zoom_factor, coord[1] * self.zoom_factor

    ZoneToPixelLocation = {
        1: (390, 940),
        2: (250, 940),
        3: (110, 940),
        4: (390, 785),
        5: (250, 785),
        6: (110, 785),
        7: (390, 700),
        8: (250, 700),
        9: (110, 700),
        10: (390, 695),
        11: (250, 695),
        12: (110, 695),
        13: (390, 570),
        14: (250, 570),
        15: (110, 570),
        16: (390, 500),
        17: (250, 500),
        18: (110, 500),
        19: (390, 430),
        20: (250, 430),
        21: (110, 430),
        22: (390, 305),
        23: (250, 305),
        24: (110, 305),
        25: (390, 200),
        26: (250, 200),
        27: (110, 200),
        28: (390, 115),
        29: (250, 115),
        30: (110, 115),
        31: (390, 40),
        32: (250, 40),
        33: (110, 40),
    }
