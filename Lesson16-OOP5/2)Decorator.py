class Personel:
    def __init__(self,isim,soyisim):
        self.FirstName = isim
        self.LastName  = soyisim

    @property
    def email(self):
        return  "{}.{}".format(str(self.FirstName).lower(),str(self.LastName).lower())

    @property #isim_soyisim alanında property olarak belirliyoruz.
    def isim_soyisim(self):
        return "{} {}".format(self.FirstName,self.LastName)

    @isim_soyisim.setter
    def isim_soyisim(self,parametre):
        ad, soyad      = parametre.split(" ")
        self.FirstName = ad
        self.LastName  = soyad

    @isim_soyisim.deleter
    def isim_soyisim(self):
        print("Kişi Silindi !")
        self.FirstName = None
        self.LastName = None


per1 = Personel("Berke", "Aksu")
print(per1.FirstName) #Berke
print(per1.LastName)  #Aksu
print(per1.email)     #berke.aksu

per1.isim_soyisim = "Ahmet Şahin"
print(per1.FirstName) #Ahmet
print(per1.LastName)  #Şahin
print(per1.email)     #ahmet.şahin

del per1.isim_soyisim
print(per1.FirstName)
print(per1.LastName)
print(per1.email)