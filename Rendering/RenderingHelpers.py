class RenderingHelper:
    zoom_factor: float = 1.0

    def __init__(self, zoom_factor: float):
        self.zoom_factor = zoom_factor

    def get_centre_of_zone(self, zone_num: int):
        coord = self.ZoneToPixelLocation[zone_num]
        return coord[0] * self.zoom_factor, coord[1] * self.zoom_factor

    ZoneToPixelLocation = {
        1: (110, 35),
        2: (250, 35),
        3: (390, 35),
        4: (110, 110),
        5: (250, 110),
        6: (390, 110),
        7: (110, 200),
        8: (250, 200),
        9: (390, 200),
        10: (110, 305),
        11: (250, 305),
        12: (390, 305),
        13: (110, 430),
        14: (250, 430),
        15: (390, 430),
        16: (110, 500),
        17: (250, 500),
        18: (390, 500),
        19: (110, 570),
        20: (250, 570),
        21: (390, 570),
        22: (110, 695),
        23: (250, 695),
        24: (390, 695),
        25: (110, 800),
        26: (250, 800),
        27: (390, 800),
        28: (110, 885),
        29: (250, 885),
        30: (390, 885),
        31: (110, 950),
        32: (250, 950),
        33: (390, 950),
    }
