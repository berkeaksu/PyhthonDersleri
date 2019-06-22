try:
    number = int(input("Lütfen birinci sayiyi giriniz : "))
    number2 = int (input("Lütfen ikinci sayiyi giriniz : "))

    toplam = number+number2
    fark = number-number2
    bolum = number/number2
    carpim = number*number2

    print("Sayilarin toplamı : ",toplam,
          "\nSayıların farkı : ",fark,
          "\nSayıların bölümü : ",bolum,
          "\nSayıların çarpımı : ",carpim)

except (ValueError,SyntaxError):
    print("Value Error hatası veya Syntax Error hatası")
except ZeroDivisionError:
    print("Zero Division Error hatası")
except FileExistsError:
    print("File Exists Error")
except:
    print("Hata mesajı")