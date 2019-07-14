a = 40 # Değeri 40 olan sayısal bir <class 'int'> tipinde bir değişken tanımladık.

b = a # b değişkeni tanımlayıp referansını a değişkeninden aldık

c = [b] # c değişkeni tanımlayıp <class 'list'> b değerini referans olarak verdik.

print(type(a))
print(a)
del a # A değişkeninin referansın sildik.
#print(a)

b = 100 # b değerine 100 değerini vererek üzerinde yer alan 40 değerini değiştirdik.
print(b)

print(type(c))
c[0] = -1 # c listesinin 0. elemanının değerini -1 olarak değiştirerek 40 değerini sildik ve a değişkenine ait hiç bir referans kalmamıştır.
print(c[0])


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "Heap üzerinden silindi")


pt1 = Point()
pt2 = pt1
pt3 = pt1

print(id(pt1), id(pt2), id(pt3)) # Nesnenin ram adresi değerinin ekrana yazdırılması

# pt1 => 10156272
# pt2 => 10156272
# pt3 => 10156272

del pt1, pt2
print(id(pt3))

# id() Nesnenin kimliğini döndürür. Nesne yaşam ömrü boyunca benzersiz ve sabit olacağı garantilenen(uniq) bir tam sayıdır. Birbirinden benzersiz iki nesne aynı değere sahip olabilirler.