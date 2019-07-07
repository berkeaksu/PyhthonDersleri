

def decorator(metot):

    def sarmal_metot():
        print("Sarmal metodu {} 'dan önce tetiklendi.".format(metot.__name__))
        return metot()

    return sarmal_metot



@decorator # Altındaki metodu parametre olarak alır.
def Print_Metot():
    print("Print_Metot Çalıştı")


Print_Metot()


#Sarmal metodu Print_Metot 'dan önce tetiklendi.
#Print_Metot Çalıştı