# .append() = dizi içerisine eleman eklemek için kullanılır. (JS dilinde de aynı yöntem geçerlidir.)
# .append() ekleme işlemini dizinin sonuna yapar.

sehirler = []

sehirler.append("Ankara")
sehirler.append("İstanbul")
sehirler.append("Edirne")
sehirler.append("İstanbul")
sehirler.append("İzmir")
sehirler.append("Malatya")

print(sehirler[:])

#----------------------------------------------------------------------------------------------------------

# .insert() = dizinin içerisinde belirtilen alana(indexe) ekleme işlemi yapar

sehirler.insert(1,"Sivas")

print(sehirler[:])

#-----------------------------------------------------------------------------------------------------------

# .count() = dizi içerisinde yer alan elemanların, list içerisinde kaç defa geçtiğini return eder.

print("Dizi içerisinde İstanbul", sehirler.count("İstanbul"), "adet içermektedir.")

#-----------------------------------------------------------------------------------------------------------

# .pop() = dizi içerisinde eleman silme, parametre verilirse; verilen index değerindeki elemanı siler, verilmez ise dizinin en son elemanını siler.
# .pop() methodunun özelliği silinen elemanı return etmesidir.

print(sehirler[:])
#print(sehirler.pop(1))
print(sehirler[:])

print(sehirler.pop())
print(sehirler[:])

#------------------------------------------------------------------------------------------------------------

# .remove() = dizi içerisinden eleman silme, eleman silmek için object ister.
# Eğer içeride aynı değere sahip eleman var ise soldan sağa doğru bulduğu ilk elemanı silecektir.
# Değer return etmez.


print(sehirler.remove("İstanbul"))
print(sehirler[:])

#-------------------------------------------------------------------------------------------------------------

# .sort() = dizini elemanlarını A'dan Z'ye, 0'dan 9'a sıralama işlemi yapar.

sehirler.sort()
print(sehirler[:])

#-------------------------------------------------------------------------------------------------------------

# .reverse() = dizi içerisindeki elemanları tersine çevirir, kesinlikle sıralama işlemi yapmaz, diziyi olduğı gibi tersten yazdırır.

sehirler.reverse()
print(sehirler[:])

#-------------------------------------------------------------------------------------------------------------

print(len(sehirler))
print(sehirler[:])

del sehirler # dizinin tamamını siler.




