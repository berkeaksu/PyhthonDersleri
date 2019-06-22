try:
    sayi1 = int(input("Lütfen bölünecek sayıyı giriniz : "))
    sayi2 = int(input("Lütfen bölecek sayıyı giriniz : "))

    #sonuc = sayi1/sayi2
    #print("İşlem Sonucu : ",sonuc)

except ValueError as exp:
    print("İşlem hatası : ",exp)
else:
    try:
        print(sayi1/sayi2)
    except ZeroDivisionError:
        print("Sayi 0 değerine bölünemez")