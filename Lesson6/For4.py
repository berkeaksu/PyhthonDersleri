#Dısarıdan girilen metri harf harf alt alta yazdırınız.

string = input("Lütfen bir metin giriniz : ")
result = ""
for harf in string:
    result += harf +"-"

print(result)

print("-".join(string))