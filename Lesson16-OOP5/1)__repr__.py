import datetime
now = datetime.datetime.now()

print(str(now))
#2019-07-21 10:21:20.236668

print(repr(now))
#datetime.datetime(2019, 7, 21, 10, 22, 2, 890202

class Personel:
    def __init__(self,isim):
        self.FirstName = isim

    def __repr__(self):
        return  "Personel ( '{}', '{}' )".format(self.FirstName,self.FirstName)

    def __str__(self):
        return "{}-{}".format(self.FirstName,self.FirstName)


per = Personel("Berke")
print(str(per))            #Berke-Berke
print(repr(per))           #Personel ( 'Berke', 'Berke' )
print(str(per))            #Berke-Berke

print(per.__repr__())      #Personel ( 'Berke', 'Berke' ) #developer için devam niteliğinde kod verir.
print(per.__str__())       #Berke-Berke                   #son kullanıcı için çıktı verir.
