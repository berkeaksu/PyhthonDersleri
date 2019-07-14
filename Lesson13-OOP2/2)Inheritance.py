class Calısan():

    def __init__(self,isim,soyisim,maas,departman,yas = 10):
        print("Çalışan sınıfı yapıcı metodu çalıştı!")
        self.isim      = isim
        self.soyisim   = soyisim
        self.yas       = yas
        self.maas      = maas
        self.departman = departman

    def __str__(self):
        return "{} {} {}\n".format(self.isim,self.soyisim,self.yas)

    def BilgiGoster(self):
        print("Çalısan Sınıfına ait bilgiler gösterilmektedir!\n")
        print("-"*30)
        print("İsim : {}\nSoyisim : {}\nDepartman : {}\nMaaş : {}\n".format(self.isim,
                                                                            self.soyisim,
                                                                            self.departman,
                                                                            self.maas))

    def ZamYap(self,zam_orani):
        eskimaas = self.maas
        print("Çalışanın Maaşına Zam Yapıldı!")
        self.maas += zam_orani
        print("{} {} personeli maası {} TL'den {} TL'ye yükseltildi.\n".format(self.isim,self.soyisim,eskimaas,self.maas))


    def DepartmanDegistir(self,departman):
        eskidep=self.departman
        print("Çalışanın Departmanı Değiştirildi!")
        self.departman = departman
        print("{} {} personeli {} departmanından {} departmanına geçti.\n".format(self.isim, self.soyisim, eskidep,
                                                                               self.departman))



#personelin maaşına zam yapıldığında veya departmanı değiştirildğinde, kullanıcıya eski değer ve yeni değerleri gösteriniz.
#A personeli X departmanından Y departmanına gecti.
#A personeli maası X TL'den Y TL ye yükseltildi.


#personel = Calısan("Murat","Vuranok") #yas parametresi gönderilmezde default deger gecerli olacaktır.
#personel = Calısan("Murat","Vuranok",5000,"Yazılım",99)

#print(personel)
#personel.ZamYap(1000)
#personel.DepartmanDegistir("Operasyon")
#personel.BilgiGoster()


class Yonetici(Calısan): #yönetici sınıfına calısan sınıfını miras veriyorum
    def __init__(self,isim,soyisim,maas,departman,yas,kisi_sayisi):
        print("Yönetici sınıfı yapıcı metodu çalıştı!\n")
        self.isim        = isim
        self.soyisim     = soyisim
        self.departman   = departman
        self.maas        = maas
        self.kisi_sayisi = kisi_sayisi
        self.yas         = yas
    def disBase(self):
        for base in self.__class__.__bases__:
            print("Miras Alınan Sınıf  :",base.__name__)

    #Calısan class ındaki __str__ metodunu ezmek istersek burada tekrara bir __str__ metodu oluşturmamız gerekir.

yonetici = Yonetici("Ahmet","Mehmet",10000,"Teknoloji Müdürü",40,355)
print(yonetici)
yonetici.disBase()
yonetici.BilgiGoster()
yonetici.ZamYap(2000)
yonetici.DepartmanDegistir("Genel Müdür")