from dataclasses import dataclass

from .technique import Technique


@dataclass
class Booking:
    technique: Technique

    def __repr__(self):
        return f'{self.__class__.__name__}({self.technique})'
