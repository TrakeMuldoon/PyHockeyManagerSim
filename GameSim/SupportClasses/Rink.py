from GameSim.SupportClasses.Zones import Zone


class Rink:
    _ROW_WIDTH = 3
    _NUM_ROWS = 11
    _MAX_ZONE = 33

    @staticmethod
    def up_ice(zone: Zone):
        row = (zone.value - 1) // Rink._ROW_WIDTH
        return Zone(zone.value + 3) if row < (Rink._NUM_ROWS - 1) else zone

    @staticmethod
    def down_ice(zone: Zone):
        row = (zone.value - 1) // Rink._ROW_WIDTH
        return Zone(zone.value - 3) if row > 0 else zone

    @staticmethod
    def right_ice(zone: Zone):
        col = (zone.value - 1) % Rink._ROW_WIDTH
        return Zone(zone.value + 1) if col < (Rink._ROW_WIDTH - 1) else zone

    @staticmethod
    def left_ice(zone: Zone):
        col = (zone.value - 1) % Rink._ROW_WIDTH
        return Zone(zone.value - 1) if col > 0 else zone
