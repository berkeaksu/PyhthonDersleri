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


#Kullanım Yöntemleri :

# Class içerisinde tanımlanmış metotlara ulaşma :
# 1)
Ogrenci.NotVer("","Murat Vuranok")
Ogrenci.CezaVer("","Murat Vuranok")
Ogrenci.YoklamaGir("","Murat Vuranok")


