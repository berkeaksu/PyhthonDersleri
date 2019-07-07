# Dısarıdan girilen 2 sayının toplamını ekrana yazdırma
# Kural 1 : Kesinlikle metot içerisine parametrenin nereden geleceği tanımlanmaz!
# Kural 2 : Kesinlikle metot içerisinde parametreye değer atanmaz!

def Hesapla(a,b):
    toplam = a+b
    print(toplam)


sayi1=int(input("1.sayi : "))
sayi2=int(input("2.sayi : "))

Hesapla(sayi1,sayi2)