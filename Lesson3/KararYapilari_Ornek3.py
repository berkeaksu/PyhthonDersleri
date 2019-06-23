# Mantıksal Operatorler
#----------------------
# and => Sorguya katılan her bir koşulun sağlanması
# or => Sorguya katılan herhangi bir koşulun sağlanması
# not => Sorgula olumsuzlık katar; True ise False, False ise True döndürür.



user_name = input("Lütfen kullanıcı adınızı giriniz : ")


if user_name == "admin" : # db içerisinde var mı ?
    password = input("Lütfen şifrenizi adınızı giriniz : ")
    if password == "123":
        print("Giriş yaptınız !")
    else:
        print("Şifreniz yanlış.")
else:
    print("Kullanıcı adınız yanlış.")


user_name = input("Lütfen kullanıcı adınızı giriniz : ")
password = input("Lütfen şifrenizi adınızı giriniz : ")

if user_name == "admin" and password ==  "123":
    print("Tebrikler!")
else:
    print("Kullanıcı bilgilerinizi kontrol ediniz.")