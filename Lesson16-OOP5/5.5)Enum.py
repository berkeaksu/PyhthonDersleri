from enum import Enum


class Durum(Enum):
    Mutlu = 1
    Uzgun = 3

    def describe(self):
        return self.name,self.value

    def __str__(self):
        return "Şu anki ruh halim {}".format(self.name)

    @classmethod
    def favori_durum(cls):
        return  cls.Uzgun



print(Durum.favori_durum())
print(Durum.Uzgun.describe())
print(str(Durum.Mutlu))