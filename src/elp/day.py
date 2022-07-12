from datetime import date

from .shift import ShiftTime
from .technique import Technique
from .etching_relief import EtchingReliefShift
from .screenprinting_fabric import ScreenprintingFabricShift


class Day:
    SATURDAY = 5
    SUNDAY = 6

    def __init__(self, date: date):
        self.date = date
        self.etching_relief_shifts = {ShiftTime.MORNING: EtchingReliefShift()}
        self.screenprinting_shifts = {ShiftTime.MORNING: ScreenprintingFabricShift()}
        if date.weekday() != self.SATURDAY:
            self.etching_relief_shifts[ShiftTime.AFTERNOON] = EtchingReliefShift()
            self.screenprinting_shifts[ShiftTime.AFTERNOON] = ScreenprintingFabricShift()
        if date.weekday() == self.SUNDAY:
            self.etching_relief_shifts = {}
            self.screenprinting_shifts = {}

    def get_shifts(self, technique: Technique):
        match technique:
            case Technique.ETCHING | Technique.LINO:
                shifts = self.etching_relief_shifts
            case Technique.SCREENPRINTING | Technique.FABRIC:
                shifts = self.screenprinting_shifts
        return shifts

    def book(self, shift_time: ShiftTime, technique: Technique):
        shift = self.get_shifts(technique)[shift_time]
        shift.book(technique)
