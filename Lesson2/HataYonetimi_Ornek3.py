try:
    sayi = int(input("Sayı giriniz : "))
    print("Tebrikler !!")
except:
    print("Hata aldık")
finally:
    print("Her işlem sonucunda çalışır")
    #Connection.close()