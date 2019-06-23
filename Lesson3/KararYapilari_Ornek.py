# Örnek : Girilen not değeri 0'dan küçük ise , "0'dan küçük not giremezsiniz.", 100'den büyük ise "100'den büyük
#değer giremezsiniz." uyarısı yapan uygulama.



try:
    note = float(input("Lütfen not değerini giriniz :"))

    if (note > 100):
        print("100'den büyük değer giremezsiniz.")
    elif (note < 0):
        print("0'dan küçük değer giremezsiniz.")
    else:
        print("Girilen Not Değeri", note)

except ValueError as exp:
    print("Lütfen sayısal değer giriniz")
except Exception as exp:
    print("Belirlenemeyen bir hata ile karşılaşıldı")
