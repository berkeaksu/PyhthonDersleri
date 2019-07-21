#Flag kullanımı, olusturduğunuz enum değerlerinin sayısal karşılığının

from enum import Enum, auto, Flag

class Renkler(Flag):
    Kirmizi   = auto() # Enum =>1 , Flag =>1
    Sari      = auto() # Enum =>2 , Flag =>2
    Mavi      = auto() # Enum =>3 , Flag =>4
    Turuncu   = auto() # Enum =>4 , Flag =>8
    Yesil     = auto() # Enum =>5 , Flag =>16
    Pembe     = auto() # Enum =>6 , Flag =>32
    Beyaz     = Kirmizi | Mavi | Sari  # Flag =>7


#print(repr(Renkler.Sari and Renkler.Mavi))

liste = list(Renkler)
print(liste)

print(Renkler.Kirmizi.value+Renkler.Mavi.value+Renkler.Sari.value) #7
print(repr(Renkler.Beyaz)) #<Renkler.Beyaz: 7>
