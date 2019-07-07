def Mail(ad:str, soyad:str, domain:str = "bilgeadam") -> str:

    return "{}.{}@{}.com".format(ad,soyad,domain)


def Mail1(ad, soyad, domain):
    return "{}.{}@{}".format(ad, soyad, domain)


print(Mail("berke","aksu","gmail"))
print("Mail metotdunun geriye dönüş tipi : ", Mail.__annotations__)
print("Mail1 metotdunun geriye dönüş tipi : ", Mail1.__annotations__)