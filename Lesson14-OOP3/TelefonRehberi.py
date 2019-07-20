import random

#'''
class Person:
    FirstName = ""
    LastName  = ""
    Phone     = ""
    Mail      = ""

    def __str__(self):
        return "{} {}".format(self.FirstName,self.LastName)

    def Bul(self,kelime):
        if kelime in self.FirstName or kelime in self.LastName or kelime in self.Mail or kelime in self.Phone:
            return True
        else:
            return False


#'''
#-------------------------------------------------------------------------------------------------------------------
persons = []

isimler = ["Ahmet","Berke","Göker","Ali","Nejat","Kaplan","Uğur","Simge","Yağmur","Ege"]
soyisimler = ["Aksu","Barlas","Çengel","Develi","Deve","Bulut","Güneş","Çolak","Erdem","Efe"]

#Default olarak kullanıcı ekleme.
for i in range(10):
    kisi = Person()
    kisi.FirstName = isimler[random.randint(0,9)]
    kisi.LastName  = soyisimler[random.randint(0,9)].upper()
    kisi.Mail      = "{}.{}@bilgeadam.com".format(kisi.FirstName.lower(),kisi.LastName.lower())
    kisi.Phone     = "+(90)5{} {} {} {}".format(random.randint(10,99),random.randint(100,999),random.randint(10,99),random.randint(10,99))
    persons.append(kisi)


#-------------------------------------------------------------------------------------------------------------------
def Liste(kelime=""):
    if kelime == "":
        index = 0
        for kisi in persons:
            print("-" * 40)
            print("ID : {}\nKisi Adı : {}\nKisi Soyadı : {}\nKisi Telefon : {}\nKisi Mail : {}".format(index + 1,
                                                                                                       kisi.FirstName,
                                                                                                       kisi.LastName,
                                                                                                       kisi.Phone,
                                                                                                       kisi.Mail))
            print("-" * 40)
            index += 1
    else:
        index = 0

        for kisi in persons:
            if kisi.Bul(kelime):
                print("-" * 40)
                print("ID : {}\nKisi Adı : {}\nKisi Soyadı : {}\nKisi Telefon : {}\nKisi Mail : {}".format(index + 1,
                                                                                                       kisi.FirstName,
                                                                                                       kisi.LastName,
                                                                                                       kisi.Phone,
                                                                                                       kisi.Mail))
                print("-" * 40)
            index += 1

#-------------------------------------------------------------------------------------------------------------------
def Main():
    ekle     = "a"
    sil      = "d"
    guncelle = "u"
    listele  = "l"
    bul      = "f"
    result = True
    while result :

        print("Lütfen yapmak istediğiniz işlemi seçiniz : ")
        print("-"*30)
        print("Kişi Eklemek İçin : a\nKişi Silmek İçin : d\nKişi Güncellemek İçin : u\nKişi Listelemek İçin : l\nKişi Bulmak İçin : f")
        print("İşleme Devam Etme İstemiyorsanız Herhangi Bir Tuşa Basınız !")
        print("-" * 30)
        islem = input("Lütfen bir anahtar harf giriniz : ").lower()

        if islem == "a" :
            kisi = Person()
            kisi.FirstName = input("Lütfen İsim Giriniz : ")
            kisi.LastName  = input("Lütfen Soyisim Giriniz : ")
            kisi.Phone     = input("Lütfen Telefon Giriniz : ")
            kisi.Mail      = input("Lütfen Mail Giriniz : ")

            persons.append(kisi)
            print("Kişi Rehbere Eklendi !")


        elif islem == "d" :
            index = 0
            for kisi in persons:
                Liste()

            id=int(input("Silmek istediğiniz kişi ID değerini giriniz :  "))
            persons.remove(persons[id-1])
            print("Kişi Rehberden Silindi !")


        elif islem == "u" :
            Liste()
            id = int(input("Lütfen Güncellemek istediğiniz kişinin ID'sini giriniz."))
            update_person = persons[id-1]

            for key,value in vars(update_person).items():
                vl = input("Lütfen {} Giriniz : ".format(key))
                vars(update_person).__setitem__(key,vl)

            '''
            update_person.FirstName = input("Lütfen İsim Giriniz : ")
            update_person.LastName  = input("Lütfen Soyisim Giriniz : ")
            update_person.Phone     = input("Lütfen Telefon Giriniz : ")
            update_person.Mail      = input("Lütfen Mail Giriniz : ")
            '''
        elif islem == "l" :
            Liste()


        elif islem == "f" :

            Liste(input("Lütfen anahtar kelime giriniz : "))


        else:
            result=False
            print("Rehber Uygulamasından Çıkış Sağlandı !")

Main()

#Kullanıcı dışarıdan telefon girdiğinde içeride formatlanması
#Metot içerisine telefon numarası alacak, geriye formatlı bir şekilde döndürecek.
#Minimum girilecek değeri 10 hanedir. Eğer kullanıcı eksik değer girerse uyarı verdiriniz.
#01111111111   => +90 (111) 111 11 11
#1111111111    => +90 (111) 111 11 11
#901111111111  => +90 (111) 111 11 11
#+901111111111 => +90 (111) 111 11 11