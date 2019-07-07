# Dısarıdan bir sayısal dizisinin parametre olarak alan bir metot yazınız. Metot, parametredeki dizide yer alan elemanların toplamının karekökünü dönsün.

import math

def WTF(a):
    toplam = 0
    for i in range(len(a)):
        toplam = toplam+a[i]

    return math.sqrt(toplam)


a = [1,2,3,4,5,6,7,8,9,10,100,257,368]

print(WTF(a))



