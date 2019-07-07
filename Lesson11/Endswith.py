# .endswith() => metnin parametrede gönderdiğiniz değer ile bitip bitmediğini True / False değer olarak döner.

metin = "murat vuranok"
sonuc = metin.endswith("ok")


if sonuc:
    print("metin ok kelimesi ile bitmektedir.")
else:
    print("metin ok kelimesi ile bitmemektedir.")


#Ternary kullanımı

print("metin ok kelimesi ile bitmektedir.") if sonuc else print("metin ok kelimesi ile bitmemektedir.")

#metin ok kelimesi ile bitmektedir.
