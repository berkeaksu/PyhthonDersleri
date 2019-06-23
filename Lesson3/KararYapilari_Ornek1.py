# Örnek : Dışarıdan girilen sayının tek veya çift olma durumunun kontrol edilmesi.Kullanıcıya sayı bilgisi verilmesi

try:
    sayi = int(input("Lütfen sayi değerini giriniz :"))

    k = sayi % 2

    if (k == 0):
        print("Sayi çifttir.")

    else:
        print("Sayi tektir.")

except ValueError as exp:
    print("Lütfen sayısal değer giriniz")
except Exception as exp:
    print("Belirlenemeyen bir hata ile karşılaşıldı")