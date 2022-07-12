from itertools import permutations

import pytest

from elp import Technique
from elp import EtchingRelief

# todo: generalize
max_etching = EtchingRelief.MAX_BOOKINGS[Technique.ETCHING]
max_lino = EtchingRelief.MAX_BOOKINGS[Technique.LINO]
max_bookings = max_etching * [Technique.ETCHING] + max_lino * [Technique.LINO]
groups = sorted(set(permutations(max_bookings)))

@pytest.mark.parametrize('booking_order', groups)
def test_etching(booking_order):
    room = EtchingRelief()
    for technique in booking_order:
        try:
            room.book(technique)
            assert room.num_bookings <= room.MAX_NUM_BOOKINGS
        except ValueError as e:
            # is_full = room.is_full()
            # assert room.num_bookings == room.MAX_NUM_BOOKINGS
            print(e)
            break
