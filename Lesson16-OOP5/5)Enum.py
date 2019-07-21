from enum import Enum

class Color(Enum):
    Red   = 1
    Green = 2
    Blue  = 3


print(Color.Blue)       #Color.Blue

print(repr(Color.Green))#<Color.Green: 2>

print(type(Color.Red))  #<enum 'Color'>

print(isinstance(Color.Red,Color)) #True

print(Color.Red.name)   #Red  => İlgili Enum değerinin adını alırsınız.

