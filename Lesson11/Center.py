# .center() => nesneye uygulandığında sağdan ve soldan eşit boşluklar verir.
# Metnin karakter uzunluğunu veirlen değerden çıkarır ve kalan değeri boşluk olarak sola ve sağa dağıtır.
metin = "bilge adam"
print(len(metin))
#10

metin = metin.center(15)
print(metin)
print(len(metin))
#   bilge adam
#15

