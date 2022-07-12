from dataclasses import dataclass

from .shift import Shift
from .technique import Technique


@dataclass
class ScreenprintingFabricRoom:
    MAX_NUM_BOOKINGS: int = 6


# Screen or fabric
# 5 screen, 1 fabric
class ScreenprintingFabricShift(Shift):
    MAX_BOOKINGS = {
        Technique.SCREENPRINTING: 5,
        Technique.FABRIC: 1,
    }

    def __init__(self):
        super().__init__()
        self.room = ScreenprintingFabricRoom()
