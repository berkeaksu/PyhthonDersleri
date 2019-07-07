# .maketrans

kaynak = "şçöğüıŞÇÖĞÜİ"
hedef = "scogüiSCOGUI"

ceviri_tablosu = str.maketrans(kaynak,hedef)
print(ceviri_tablosu)
#{351: 115, 231: 99, 246: 111, 287: 103, 252: 252, 305: 105, 350: 83, 199: 67, 214: 79, 286: 71, 220: 85, 304: 73}

metin = "Bilge Adam Bireysel Eğitimlerde Artık Python Dersleri Başlayacaktır"
print(metin)
#Bilge Adam Bireysel Eğitimlerde Artık Python Dersleri Başlayacaktır
metin = metin.translate(ceviri_tablosu)
print(metin)
#Bilge Adam Bireysel Egitimlerde Artik Python Dersleri Baslayacaktir