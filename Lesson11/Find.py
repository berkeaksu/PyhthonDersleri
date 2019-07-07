# .find(), .rfind()

# .index(), .rindex()

metin = "murat vuranok bilge adam beşiktaş yazılım"
sonuc= metin.find("a") # Verilen karakteri metin içerisinde soldan sağa doğru arama işlemi yapar. Eğer belirtilen karakter metin içerisinde var ise index değerini, yok ise -1 döner.

print(sonuc) #3

sonuc = metin.rfind("a") # Verilen karakteri metin içerisinde sağdan sola doğru arama işlemi yapar. Eğer belirtilen karakter metin içerisinde var ise index değerini, yok ise -1 döner.

print(sonuc) #35