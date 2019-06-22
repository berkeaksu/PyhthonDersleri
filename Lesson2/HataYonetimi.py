# Programcı hataları (Error)
# Program kusurları  (Bug)
# İstisnalar         (Exception)
# Mantıksal Hatalar


try :
    telefon_numarasi = input("Lütfen telefon numaranızı giriniz :")
# Telefon numarası db'ye kaydedildi.
    print("Telefon numaranız : ",int(telefon_numarasi))

except ValueError:
    print("İşlem Hatası")
    print("Lütfen geçerli bir sayi giriniz.")
except ZeroDivisionError:
    print("İşlem Hatasi")
    print("Sıfıra bölünme hatası")


