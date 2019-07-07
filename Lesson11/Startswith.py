# .endswith() => metnin parametrede gönderdiğiniz değer ile başlayıp başlamadığını True / False değer olarak döner.

metin = "bilgeadam"
sonuc = metin.endswith("bil")

print(sonuc)
#False

print("metin bil kelimesi ile başlamaktadır.") if sonuc else print("metin bil kelimesi ile başlamakatadır.")
#metin bil kelimesi ile başlamakatadır.