# Dısarıdan girilen değerin, tek veya çift olma durumuna göre geriye değer dönen metot, sayı çift ise -1, tek ise : 1 sıfıra eşit ise 0 değerini teslim etsin.

def Sayi(a):

    if a  == 0 :
        return 0
    elif a %2 == 0 :
        return -1
    else:
        return 1


deger = int(input("Bir sayı değeri giriniz : "))

print(Sayi(deger))
