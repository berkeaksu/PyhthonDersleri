# Hata mesajı

try:
    sayi = int(input("Lütfen sadece sayısal veri giriniz : "))
    print("Gelen sayi : ", sayi)
    #sayi = sayi/0
    sayi = str(sayi)/0
except ValueError as ex:
    print("ValueError")
    print("Sistem Hata Mesajı : ",ex)
except ZeroDivisionError as ex:
    print("ZeroDivisionError")
    print("Sistem Hata Mesajı : ", ex)
except Exception as ex:
    print("except")
    print("Sistem Hata Mesajı : ", ex)
