# Kullanıcı dısarıdan dilediği kadar sayi girecek, her sayı girdikten sonra sayi girmeye devam edip etmeyeceğine sorulacak.

#Kullanıcı Y veya y tusuna basarsa yeni bir sayı girmesi istenecek
#Kullanıcı harici bir tusa basarsa içeriye aldığı sayılar içerisindeki tek sayıların en buyuk ve en kucugunun farkı alınıp işlem sonucunun geriye donulecek



#def Sonuc():
 #   tek_sayilar = []
 #  sayilar = []

    #sayi = int(input("Lütfen bir sayi giriniz : "))
    #sayilar.append(sayi)

    #while(1):

        #cevap = input("sayi girmeye devam etmek istiyor musunuz ? Y/y : ").lower()

        #if cevap == 'y' :
         #   sayi = int(input("Lütfen bir sayi giriniz : "))

        #    sayilar.append(sayi)
       # else:
      #      print("Girilen Sayilar : ",sayilar[:])
     #       break

    #for i in sayilar:

      #   if i%2 !=0:
     #        tek_sayilar.append(i)

    #tek_sayilar.sort()
   # print("Girilen tek sayilar : ",tek_sayilar[:])
  #  fark = (tek_sayilar[len(tek_sayilar)-1])-(tek_sayilar[0])

 #   return fark



#print(Sonuc())



#--------------------------------------------------------------------------------------------------


def FarkHesapla():
    go_on = "y"
    tekSayilar = []
    while go_on == "y" or go_on == "Y":
        number = float(input("Lütfen bir sayi giriniz : "))
        if number%2 != 0 :
            tekSayilar.append(number)
        go_on = input("Yeni bir sayı eklemek istiyor musunuz ? (Y\\N) : ")

    return  max(tekSayilar)-min(tekSayilar)

print(FarkHesapla())