# Dısarıdan aldığı metin içerisinde yer alan sesli karakterlerin ve sessiz karakterlerin sayısını ekrana yazdıran metot

def Harfler(metin):
    sesli_harf = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    liste = list(metin)
    sesli_count = 0
    sessiz_count = 0
    index = 0

    for i in metin:

        if i in sesli_harf:
            sesli_count +=1


        else:
            sessiz_count +=1



    print("Metindeki Sesli Harf Sayısı : {}\nMetindeki Sessiz Harf Sayısı : {}".format(sesli_count,sessiz_count))



Harfler(input("Bir metin giriniz :").lower().replace(" ",""))