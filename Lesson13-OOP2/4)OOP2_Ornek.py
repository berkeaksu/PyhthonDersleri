#Ogrenci             : isim, soyisim, okul numarası, TCKN, Sınıf, mail, telefon
#Ogrentmen           : isim, soyisim,              , TCKN, Sınıf, mail, telefon, maas, brans
#Mudur Yardımcısı    : isim, soyisim,              , TCKN,      , mail, telefon, maas, gorev
#Mudur               : isim, soyisim,              , TCKN,      , mail, telefon, maas, gorev
#Memur               : isim, soyisim,              , TCKN,      , mail, telefon, maas, gorev
#Hizmetli            : isim, soyisim,              , TCKN,      ,     , telefon, maas, gorev


class BaseClass():
    isim     = ""
    soyisim  = ""
    TCKN     = ""
    mail     = ""
    telefon  = ""

    def __str__(self):
        return "{} {}".format(self.isim,self.soyisim)

class Calısan(BaseClass):
    maas = ""
    gorev = ""

class Ogrenci(BaseClass):
    okul_numarasi = ""
    sinif = ""

class Ogretmen(BaseClass):
    brans = ""
    sinif = ""
    maas =""

class MudurYardimcisi(Calısan):
    pass

class Mudur(Calısan):
    pass

class Memur(Calısan):
    pass

class Hizmetli(Calısan):
    pass





