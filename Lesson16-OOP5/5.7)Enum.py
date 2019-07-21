from enum import Enum

class Renk(Enum):
    Kirmizi = 1
    Sari    = 2
    Mavi    = "Blue"

print(repr(Renk.Mavi)) # <Renk.Mavi: 'Blue'>


class IntEnum(int,Enum):
    Kirmizi = 1
    Sari    = 2
    #Mavi    = "Mavi" # Veri tipi int olmak zorunda.

print(IntEnum.Kirmizi.value)

class FloatEnum(float,Enum):
    Kirmizi = 1
    Mavi    = 2
    Yesil   = 1.10

print(FloatEnum.Yesil.value)