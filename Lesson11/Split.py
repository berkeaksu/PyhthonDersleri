# .split() => İçerisinde verilen parametreye göre soldan sağa doğru ayırma işlemi gerçekleştirir.

elemanlar = "yazılım,sistem,teknik çizim,web grafik"
print(elemanlar)
#yazılım,sistem,teknik çizim,web grafik

elemanlar=elemanlar.split() # => içerisine seperator olarak kullanılacak paramete verilmez ise default olarak boşluk ile ayırır.
print(elemanlar)
#['yazılım,sistem,teknik', 'çizim,web', 'grafik']

elemanlar = "yazılım,sistem,teknik çizim,web grafik"
elemanlar = elemanlar.split(',')
print(elemanlar)

#['yazılım', 'sistem', 'teknik çizim', 'web grafik']

#---------------------------------------------------------------------------------------------------------------------

metin = "murat vuranok yazılım beşiktaş istanbul"
sonuc = metin.split(' ',2)

print(sonuc)

#['murat', 'vuranok', 'yazılım beşiktaş istanbul']