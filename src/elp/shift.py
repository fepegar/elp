import enum

from .booking import Booking
from .technique import Technique


# TODO: replace use custom exceptions


@enum.unique
class ShiftTime(str, enum.Enum):
    MORNING = 'morning'
    AFTERNOON = 'afternoon'


class Shift:
    def __init__(self):
        self.bookings = []

    def __repr__(self):
        return f'{self.__class__.__name__}({self.bookings})'

    @property
    def num_bookings(self):
        return len(self.bookings)

    def is_full(self):
        return self.num_bookings >= self.room.MAX_NUM_BOOKINGS

    def check_not_full(self):
        if self.is_full():
            raise ValueError(f'The room is full: {self.bookings}')

    def add_booking(self, booking):
        self.check_not_full()
        max_bookings_technique = self.MAX_BOOKINGS[booking.technique]
        if self.num_bookings == max_bookings_technique:
            raise ValueError(f'No more bookings available for {booking.technique}: {self.bookings}')
        self.bookings.append(booking)

    def book(self, technique: Technique):
        booking = Booking(technique)
        self.add_booking(booking)

    def remove_booking(self, technique: Technique):
        for booking in self.bookings:
            if booking.technique == technique:
                self.bookings.remove(booking)
                break

    def unbook(self, technique: Technique):
        self.remove_booking(technique)
