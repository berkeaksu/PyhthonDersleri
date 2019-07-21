from enum import Enum, unique

@unique
class Icecek(Enum):
    Vanilya   = 7
    Cikolata  = 4
    Visne     = 3
    Muz       = 1
    #Kiraz     = 7 => Sınıfı Unique olarak işaretlerseniz, sınıf içeriisnden aynı index değerine sahip değişken bulunduramazsınız.

for x in Icecek:
    print(x)

for ad, uye in Icecek.__members__.items():
    print(str(ad)+" "+str(uye))
    print(str(ad),str(uye))
    print(ad, uye)
