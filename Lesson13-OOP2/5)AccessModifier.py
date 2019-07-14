class Cup1:
    def __init__(self):
        self.color   = None #public variable
        self.content = None #public variable

    def fill(self,beverage):
        self.content = beverage

    def empty(self):
        self.content = None

    def __str__(self):
        return self.color + " " + self.content


cup1 = Cup1()
cup1.color = "Red"
cup1.content = "Tea"

print(cup1)
cup1.empty()
cup1.content = "Coffee"
print(cup1)




class Cup2:
    def __init__(self):
        self.color    = None #public variable (property)
        self._content = None #protected variable
    #Korumali üye, C# gibi dillerde miras alınan sınıflarda görünse de Python dilinde; tekbir _ çizgisi var ise bana dokunma anlamına gelir.

    def fill(self,beverage):
        self._content = beverage

    def empty(self):
        self._content = None

    def __str__(self):
        return self.color + " " + self._content


cup2 = Cup2()
cup2.color    = "Blue"
cup2._content = "Tea"

print(cup2)


class Cup3:
    def __init__(self,color):
        self._color    = color #protected variable (property)
        self.__content = None  #private variable

    def fill(self,beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

    def __str__(self):
        return self._color + " " + self.__content


cup3 = Cup3("Blue")
cup3._Cup3__content = "Coffee"

print(cup3)