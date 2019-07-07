metin = "bilge Adam BEŞİKTAŞ"

print(metin.lower()) # => Tüm karaktarleri küçük harfe çevirir.
print(metin.upper()) # => Tüm karakterleri büyük harfe çevirir.

#bilge adam beşi̇ktaş
#BILGE ADAM BEŞİKTAŞ


metin = metin.lower()

result = metin.islower() #tüm karakterlerin küçük olup olmadığını kontrol eder. True / False değer döner.
print(result)
#True

result = metin.isupper() #tüm karakterlerin büyük olup olamdığını kontrol eder. True / False değer döner.
print(result)
#False

