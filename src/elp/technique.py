import enum


@enum.unique
class Technique(str, enum.Enum):
    ETCHING = 'etching'
    LINO = 'lino'
    SCREENPRINTING = 'screenprinting'
    FABRIC = 'fabric'
