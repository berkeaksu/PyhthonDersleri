# Karar yapıları : if - elif - else
#-----------------------------------
# Karşılaştırma Operatörleri
#---------------------------
# == (Eşittir) Soldaki değerin sağdaki değere eşit olma durumu
# Örnek : 1 == 1 Sonuç => True
#         4 == 2 Sonuc => False
# != (Eşit Değildir) Soldaki değerin sağdaki değere eşit olmama durumu
# Örnek : 1 != 2 Sonuc => True
#         1 != 1 Sonuc => False
# > (Büyüktür) Soldaki değerin sağdaki değerden büyük olma durumu
# Örnek : 3 > 1 Sonuc => True
#         1 > 2 Sonuc => False
# < (Küçüktür) Soldaki değerin sağdaki değerden küçük olma durumu
# Örnek : 1 < 3 Sonuc => True
#         3 < 1 Sonuc => False
# >= (Büyük Eşittir) Soldaki değerin sağdaki değerden büyük veya sağdaki değere eşit olma durumu
# Örnek : 1 >= 1 Sonuc => True
#         3 >= 1 Sonuc => True
#         1 >= 2 Sonuc => False
# <= (Küçük Eşittir) Soldaki değerin sağdaki değerden küçük veya sağdaki değere eşit olma durumu
# Örnek : 1 <= 1 Sonuc => True
#         1 <= 3 Sonuc => True
#         2 <= 1 Sonuc => False


username = input("Lütfen kullanıcı adınızı giriniz : ")
username=username\
    .lower()\
    .replace("ı","i")\
    .replace("̇n","n")\
    .replace("ç","c")\
    .replace("ş","s")\
    .replace("ö","o")\
    .replace("ğ","g")
print(username)

if (username == "admin"):
    print("Giriş yaptınız")
else:
    print("Kullanıcı adınız hatalı")




