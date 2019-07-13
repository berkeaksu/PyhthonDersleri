class Ogrenci :

    '''

    self : sınıf içerisinde yer alan metodların, diğerlerinden farkı hangi sınınf içerisinde çalıştığını belirtmesidir. Self anahtar kelimesi vererek metodun bu sınıf içerisinde çalıştığını belirtmiş oluruz. Tanımlama yapılırken eklenir fakat kullanım esnasında Python bunu bizim için kendisi yapacaktır.

    '''

    Adi = ""

    def NotVer(self, ogrenci_notu):
        print(ogrenci_notu, "Adlı ogrenciye Not Verildi !")
    def CezaVer(self, ogrenci_ceza):
        print(ogrenci_ceza, "Adlı ogrenciye Ceza Verildi !")
    def YoklamaGir(self, ogrenci_yoklama):
        print(ogrenci_yoklama, "Adlı ogrencinin Yoklaması Girildi !")

class Ogrenci :

    '''

    self : sınıf içerisinde yer alan metodların, diğerlerinden farkı hangi sınınf içerisinde çalıştığını belirtmesidir. Self anahtar kelimesi vererek metodun bu sınıf içerisinde çalıştığını belirtmiş oluruz. Tanımlama yapılırken eklenir fakat kullanım esnasında Python bunu bizim için kendisi yapacaktır.

    '''

    Adi = ""

    def NotVer(self, ogrenci_notu):
        print(self.Adi, "Adlı ogrenciye {} Notu Verildi !".format(ogrenci_notu))
    def CezaVer(self, ogrenci_ceza):
        print(self.Adi, "Adlı ogrenciye {} Cezasi Verildi !".format(ogrenci_ceza))
    def YoklamaGir(self, ogrenci_yoklama):
        print(self.Adi, "Adlı ogrenci derse {}".format(ogrenci_yoklama))


#Kullanım Yöntemleri :

# Class içerisinde tanımlanmış metotlara ulaşma :


# 2)
ogrenci = Ogrenci()
ogrenci.Adi = "Murat Vuranok"
ogrenci.NotVer(50)
ogrenci.CezaVer("Disiplin")
ogrenci.YoklamaGir("Geldi")

#Murat Vuranok Adlı ogrenciye 50 Notu Verildi !
#Murat Vuranok Adlı ogrenciye Disiplin Cezasi Verildi !
#Murat Vuranok Adlı ogrenci derse Geldi


