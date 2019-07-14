from datetime import datetime
from datetime import timedelta
class Personel :

    FirsName = ""
    LastName = ""
    Phone    = ""
    Mail     = ""
    #Personelin işe giriş tarihi sistemden default verilmektedir.
    HireDate = "{}/{}/{} {}:{}".format(datetime.now().year,
                                       datetime.now().month,
                                       datetime.now().day,
                                       datetime.now().hour,
                                       datetime.now().minute)
    FireDays = 0
    Address  = ""

    def IseAl(self):
       print("Personel Adı : {:<60}\nPersonel Soyadı : {:<60}\nPersonel Maili : {:<60}\nPersonel Telefonu : {:<60}\nPersonel İşe Giriş Tarihi : {:<60}\nPersonel Adres : {:<60}\nPersonel Sözleşme Bitiş Tarihi : {:<60}\nPersonel işe girişi yapıldı !\n".format(
           self.FirsName,
           self.LastName,
           self.Mail,
           self.Phone,
           self.HireDate,
           self.Address,
           "{}/{}/{} {}:{}".format((datetime.now()+timedelta(days=self.FireDays)).year,
                                   (datetime.now()+timedelta(days=self.FireDays)).month,
                                   (datetime.now()+timedelta(days=self.FireDays)).day,
                                   (datetime.now()+timedelta(days=self.FireDays)).hour,
                                   (datetime.now()+timedelta(days=self.FireDays)).minute)
       ))
    def KayıtGuncelle(self):
        # Personel bilgilerini güncelle
        pass
    def Kov(self):
        # Personel bilgisini db den sil
        pass


time = datetime.now()

personel = Personel()
personel.FirsName = "Berke"
personel.LastName = "Aksu"
personel.Phone    = "+905309691590"
personel.Mail     = "berkeaksu13@gmail.com"
#personel.HireDate = "{}/{}/{} {}:{}".format(time.year,time.month,time.day,time.hour,time.minute)
personel.FireDays = 150
personel.Address  = "İstanbul/Besiktas"


personel.IseA()