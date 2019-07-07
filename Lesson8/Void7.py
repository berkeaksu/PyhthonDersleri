# Dısarıdan aldığı ismi ve soyisime göre mail adresi oluşturan metot. (isim.soyisim@bilgeadam.com)
# Kulanıcı 2. parametreye değer girmeyebilir.

def Mail(a,b = None):
    mail = ""
    if b is None:
        mail ="{}@bilgeadam.com".format(a)

    else:
        mail = "{}.{}@bilgeadam.com".format(a,b)

    print(mail)

#isim = input("İlk isminizi giriniz :").lower()
#soyisim = input("Soyisminizi giriniz : ").lower()

Mail(input("İlk isminizi giriniz :").lower())
Mail(input("İlk isminizi giriniz :").lower(),input("Soyisminizi giriniz : ").lower())
