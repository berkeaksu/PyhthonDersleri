# __str__ C# 'ta ToString() metodunun karışılığıdır. Class'ın override edilmesi

class Personel:
    isim = ""
    soyisim = ""
    yas = 0

    def __str__(self):
        return "{} {}".format(self.isim,self.soyisim)



p = Personel()
p.isim = "Murat"
p.soyisim = "Vuranok"
p.yas = 88

#print(p) # <__main__.Personel object at 0x0103F8F0> İlgili sınıfın ram(heap) üzerindeki adresi

print(p.isim + " " + p.soyisim)

print(p)
print(p)
print(p)
print(p)
print(p)
