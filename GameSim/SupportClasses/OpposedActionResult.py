from enum import Enum


class OpposedActionResult(Enum):
    CLEAN_WIN = 1
    CONTESTED_WIN = 2
    CONTESTED_LOSS = 3
    CLEAN_LOSS = 4

    def is_win(self):
        return self in (OpposedActionResult.CLEAN_WIN, OpposedActionResult.CONTESTED_WIN)
