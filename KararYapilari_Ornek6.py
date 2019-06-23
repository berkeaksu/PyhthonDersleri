# Örnek : Dışarıdan girilen ürün adına göre, kullanıcıya o ürünün hang, reyonda yer aldığını söyleyen uygulama yazınız
# Domates , Biber, Patlıcan => Manav Reyonu
# Diş Macunu, Parfüm, Şampuan => Kozmetik Reyonu
# Cep Telefonu, Bilgisayar, Tablet => Teknoloji Reyonu



string = input("Lütfen ürün adını giriniz : ")

if(len(string) > 0):

    string=string.lower()\
        .replace("ş","s")\
        .replace("ğ","g")\
        .replace("ç","c")\
        .replace("ü","u")\
        .replace("ı","i")\
        .replace("ö","ü")\
        .replace(" ","")

    if (string == "domates" or string == "biber" or string == "patlıcan"):
        print("Ürün manav reyonundadır.")

    elif (string == "dismacunu" or string == "parfum" or string == "sampuan"):
        print("Ürün kozmetik reyonundadır.")

    elif (string == "ceptelefonu" or string == "bilgisayar" or string == "tablet"):
        print("Ürün teknoloji reyonundadır.")

    else:
        print("Aradığınız ürün stoklarımızda yer almamaktadır.")

else:
    mesaj = "Lütfen bir ürün adı giriniz"
    print(mesaj)