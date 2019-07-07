# .index(), .rindex()

metin = "murat vuranok bilge adam beşiktaş yazılım"
sonuc= metin.index("a") # Verilen karakteri metin içerisinde soldan sağa doğru arama işlemi yapar. Eğer belirtilen karakter metin içerisinde var ise index değerini, yok ise hata döner. (ValueError : substring not found)

print(sonuc) #3

sonuc = metin.rindex("a") # Verilen karakteri metin içerisinde sağdan sola doğru arama işlemi yapar. Eğer belirtilen karakter metin içerisinde var ise index değerini, yok ise hata döner. (ValueError : substring not found)

print(sonuc) #35