def Kayitlar(**params):
    print("-"*25)
    for key, value in params.items():
        print("{0:<7} : {1}".format(key,value))

    print("-"*25)


Kayitlar (
    Ad = "Murat",
    Soyad = "Vuranok",
    Telefon = "2661532",
    Mail = "murat.vuranok@bilgeadam.com"

)