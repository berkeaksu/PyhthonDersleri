# Dısarıdan girilen metnin içerisindeki karakterlerin sesli ve sessiz olma durumuna göre ayrı dizlere ekle, adedini kullanıcıya dön.

string = input("Lütfen bir metin giriniz : ")
string = string.lower().replace(" ","")
print(string , len(string))
sesli_harf = ["a","e","ı","i","o","ö","u","ü"]

metin_sesli = []
metin_sessiz = []
index=0


while index<len(string):

     if(sesli_harf.count(string[index])):
        metin_sesli.append(string[index])


     else:
        metin_sessiz.append(string[index])

     index+=1

print("Metindeki Sesli Harfler : ",metin_sesli[:], "\nAdedi : ",len(metin_sesli))
print("Metindeki Sessiz Harfler : ",metin_sessiz[:], "\nAdedi : ",len(metin_sessiz))