from enum import Enum


class Position(Enum):
    GOALIE = (1, "G")
    LEFT_DEFENCE = (2, "LD")
    RIGHT_DEFENCE = (3, "RD")
    LEFT_WINGER = (4, "LW")
    RIGHT_WINGER = (5, "RW")
    CENTRE = (6, "C")
    EXTRA = (7, "EX")

    def __init__(self, id: int, short: str):
        self.id = id
        self.short = short

    @classmethod
    def from_short(cls, code: str):
        for member in cls:
            if member.short == code:
                return member
        raise KeyError(f"No Position with short code '{code}'")

    @classmethod
    def from_id(cls, id: int):
        for member in cls:
            if member.id == id:
                return member
        raise KeyError(f"No Position with id '{id}'")
