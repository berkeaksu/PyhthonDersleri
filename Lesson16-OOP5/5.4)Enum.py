from enum import Enum,unique,auto

@unique
class Icecek(Enum):
    Vanilya   = auto()
    Cikolata  = auto()
    Visne     = auto()
    Muz       = auto()
    Cilek     = 35
    Kahveli   = auto()

liste = list(Icecek)

print(liste)
#[<Icecek.Vanilya: 1>, <Icecek.Cikolata: 2>, <Icecek.Visne: 3>, <Icecek.Muz: 4>, <Icecek.Cilek: 35>, <Icecek.Kahveli: 36>]
