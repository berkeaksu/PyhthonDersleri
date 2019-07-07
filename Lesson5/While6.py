sayilar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Dizi içerisinde yer alan elemanları tek ve çift olarak ayırıp ayrı ayrı dizilere eklemek, işlem sonucunda adetleri kullanıcıya bildir.

tek_sayilar = []
cift_sayilar = []
counterc = 0
countert= 0

index = 0

while index < len(sayilar):

    if (sayilar[index]%2 ==0):
        cift_sayilar.append(sayilar[index])
        counterc+=1
    else:
        tek_sayilar.append(sayilar[index])
        countert+=1

    index+=1

print("Çift Sayı Dizisi : ",cift_sayilar, "\n Çift Sayı Adedi :" , counterc )
print("Tek Sayı Dizisi : ",tek_sayilar, "\n Tek Sayı Adedi :" , countert )