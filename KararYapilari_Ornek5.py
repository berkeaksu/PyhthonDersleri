try:
    note = float(input("Lütfen not değerini giriniz : "))
    mesaj = "Harf Notunuz : "
    if (note >= 0 and note <=100):

        if (note <= 30):
            mesaj += "FF"
        elif (note < 50):
            mesaj += "DD"
        elif (note < 70):
            mesaj += "CC"
        elif (note < 85):
            mesaj += "BB"
        else:
            mesaj += "AA"
    else:
        print("100'den büyük ve 0'dan küçük değer giremezsiniz.")
    print(mesaj)

except ValueError as exp:
    print("Lütfen sayısal değer giriniz")
except Exception as exp:
    print("Belirlenemeyen bir hata ile karşılaşıldı")