from dataclasses import dataclass

from .shift import Shift
from .technique import Technique


@dataclass
class EtchingReliefRoom:
    MAX_NUM_BOOKINGS: int = 7


class EtchingReliefShift(Shift):
    MAX_BOOKINGS = {
        Technique.ETCHING: 6,
        Technique.LINO: 2,
    }

    def __init__(self):
        super().__init__()
        self.room = EtchingReliefRoom()
