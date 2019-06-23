# Örnek : Disaridan sipariş alinacak kitap miktarı girilsin. Sipariş sayısı 20'den az ise toplam ücretten %5, 20-50 aralığında ise %10, 50-100 aralığında ise %15, 100'den fazla ise %25 indirim yapılsın. Kitap birim fiyatı 5 TL'dir. Amac ödenecek tutarı kullanıcıya göstermek.

try:
    sayi = int(input("Lütfen alınacak kitap miktarını giriniz : "))
    tutar = sayi * 5
    mesaj = " Ödenecek tutar : "


    if (sayi < 20):

        tutar = tutar - (tutar * 0.05)

    elif(sayi < 50):

        tutar = tutar - (tutar * 0.1)

    elif(sayi < 100):

        tutar = tutar - (tutar * 0.15)

    else:
        tutar = tutar - (tutar * 0.25)

    print(mesaj, tutar)

except ValueError as exp:
    print("Lütfen sayısal değer giriniz")
except Exception as exp:
    print("Belirlenemeyen bir hata ile karşılaşıldı")