# __init__ Constructor - yapıcı metot

class Personel:
    isim    = ""
    soyisim = ""
    yas     = 0

    def __str__(self):
        return "{} {}".format(self.isim,self.soyisim)
    def __init__(self, firstname, lastname, age):
        self.isim    = firstname
        self.soyisim = lastname
        self.yas     = age


# __init__ metodu tanımaldığımızdan dolayı artık aşağıdaki kullanım şekli çalışmayacaktır.
#personel = Personel()
#personel.isim = "Murat"
#personel.soyisim = "Vuranok"
#personel.yas = 100

#print(personel)

employee = Personel("Murat","Vuranok",100)
print(employee)