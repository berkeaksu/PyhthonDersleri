
# sorted() => Dizi içerisinde yer alan elemanların A'dan Z'ye; 0'dan 9'a  sıralama yapar.

sonuc = sorted("bilgeadamçğ") #Türkçe karakterleri dizinin en sonuna atar.

print(sonuc)

#['a', 'a', 'b', 'd', 'e', 'g', 'i', 'l', 'm', 'ç', 'ğ']

# Alfabetik oalrak değiş ASCII kod üzerinden devam eder. Düzeltmek için :

import locale # En yukarı tanımlarsak global olur.
locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")#Windows için
#locale.setlocale(locale.LC_ALL,"tr_TR")#GNU / Linux için


sonuc = sorted("bigeadamğüişçö", key=locale.strxfrm)
print(sonuc)

#['a', 'a', 'b', 'ç', 'd', 'e', 'g', 'ğ', 'i', 'i', 'm', 'ö', 'ş', 'ü']