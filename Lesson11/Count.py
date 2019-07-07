# .count => metin ya da dizi içerisinde parametrede verilen değerin adet bilgisini teslim eder.

metin = "bilge adam beşiktaş"

sonuc= metin.count("b")

print("Metin içerisinde toplamda verdiğiniz paramete {} adet içermektedir. ".format(sonuc))
#Metin içerisinde toplamda verdiğiniz paramete 2 adet içermektedir.


metinler = ["ankara", "edirne", "istanbul", "ankara", "eskisehir"]

result = metinler.count("ankara")
print(result)
#2

metin = "murat vuranok"
sonuc = metin.count("u") # =>2
print(sonuc)
sonuc=metin.count("u",2) # =>1 ikinci parametrede verilen değer, başlangıcın index değeridir. Arama işlemine 2. indexten başla
print(sonuc)


metin = "bilge adam beşiktaş yazılım dersleri, klima ön tarafı soğutmasada arkada kış ayları estirmektedir."

sonuc = metin.count("a")
print("a karakterinin metin içerisindeki toplam adedi : ", sonuc)
#a karakterinin metin içerisindeki toplam adedi :  15

sonuc = metin.count("a",6,20) # => a karakterini 6.index değerinden başlayarak 20. index değerine kadar ara
print(sonuc)
#3