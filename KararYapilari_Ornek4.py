# Örnek : Dışarıdan girilen notun bilgisi

try:
    note = float(input("Lütfen not değerini giriniz : "))
    mesaj = "Harf Notunuz : "
    if not(note > 100 and note <0):

        if (note >= 85 and note <= 100):
            mesaj += "AA"
        elif (note >= 70 and note < 85):
            mesaj += "BB"
        elif (note >= 50 and note < 70):
            mesaj += "CC"
        elif (note >= 30 and note < 50):
            mesaj += "DD"
        else:
            mesaj += "FF"
    else:
        print("100'den büyük ve 0'dan küçük değer giremezsiniz.")
    print(mesaj)

except ValueError as exp:
    print("Lütfen sayısal değer giriniz")
except Exception as exp:
    print("Belirlenemeyen bir hata ile karşılaşıldı")
