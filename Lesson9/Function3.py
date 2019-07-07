# Dısarıdan girilen ilk kelimenin ilk iki harfini buyuk, geri kalanını kucuk alınız..
# ikinci kelimenin icerisinde gecen tum a'ları e ile degistiriniz. ve sonuna @hotmail.com ekleyerek geri döndürünüz.


def MailAdresi(a, b):

    a  = a[0:2].upper() + isim[2:].lower()
    b = b.replace("a","e")

    mail = "{}.{}@hotmail.com".format(a,b)

    return mail


isim = input("İsminizi giriniz : ")

soyisim = input("Soyismizi giriniz : ")


print(MailAdresi(isim,soyisim))