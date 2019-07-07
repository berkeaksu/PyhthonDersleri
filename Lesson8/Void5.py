# 1 ile 1000 arasındaki sayıların birbirine toplamını ekrana yazdırınız.

def Toplam():
    toplam = 0
    for i in range(1,1001):
        toplam = toplam+i
    print("1 ile 1000 arasındaki sayıların toplamı : ",toplam)

Toplam()