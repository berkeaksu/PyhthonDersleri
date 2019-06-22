#print("Hello World")
#Yorum satiridir.


#Degisken tanimlama kurallari
#1) Degisken ismi sayi ile baslayamaz.
#2) Degisken iki kelimeden olusamaz(ayrik)
#3) Degisken ismi icerisinde sadece izin verilen özel karakterler kullanilabilir.(_)
#4) Degisken tanimlamasi yapilirken kesinlikle tanimli anahtar kelime kullanilamaz.
#5) Degisken ismi icerinde Turkce karakter kullanmayiniz.



# int, string, float

number = 5 #int tam sayi veri tipi
print(number)
print(type(number))

decimal_number = 4.6
print(decimal_number)
print(type(decimal_number))

my_name = "Berke"
firstName = 'Ahmet' #String tanimlarken "" veya '' kullanilabilir.
print(firstName+" "+my_name)
print(type(firstName+" "+my_name))
lastName = "Aksu"

fullname = firstName+" "+my_name+" "+lastName
print("Kullanici Adi:",fullname)

x = True
y = False

print(x)
print(y)

print(type(x))
print(type(y))



print((fullname+"\n")*5)


######################################################################################


# Convert :  Elinizdeki bir veri tipine cevirmek icin kullanilir.

# int()
# str()
# float()
# chr()
# ord() : verilen karakterin sayisal ASCII kod degerini dondurur

#var_number = input("Lutfen bir sayi giriniz : ")
#var_number1 = input("Lutfen bir sayi giriniz : ")


# result = int(var_number) + int(var_number1)

#result = float(var_number) + float(var_number1)

#print("Islem Sonucu :" ,result)
#print(type(result))
#print("Islem Sonucu : " +str(result)) #String halde yazimi

print("""
      Bilge
      Adam
      Besiktas""")

print("Bilge Adam \"Besiktas\" Istanbul") # Bilge Adam "Besiktas" Istanbul

# "bilge adam"
# 'bilge adam'
# """bilge adam"""

print("Bilge Adam \"Besiktas\" Istanbul\n\
yazilim dersleri\
python ogreniyoruz")


print(chr(65),ord('A'))
print(chr(97),ord('a'))
print(chr(90),ord('Z'))
print(chr(122),ord('z'))











