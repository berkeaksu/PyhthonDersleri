from abc import ABCMeta, abstractmethod

class BaseClass(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    @abstractmethod
    def printHam(self):
        pass # bir şey return etmeye gerek yok.

    isim = ""
    soyisim = ""

class Personel(BaseClass):
    departman = ""

    def printHam(self):
        return "personel"


per = Personel()
print(per.printHam())