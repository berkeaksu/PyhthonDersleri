# Örnek : Dışarıdan girilen kelimenin uzunluk değeri 8 karakter veya daha uzun ise "Şifre Onaylandı!" değil ise, "Şifreniz 8 Karakter veya daha uzun olmalıdır."




password = input("Lütfen Şifrenizi belirleyiniz : ")
password_length = len(password) # len() => Bu method girile değerin uzunluğunu döndürür.
print(password_length)

if (password_length >= 8):
    print("Şifreniz onaylandı !")

else:
    print("Şifreniz 8 Karakter veya daha uzun olmalıdır.")


