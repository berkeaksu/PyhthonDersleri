# Dısarıdan gelecek olan parametre sayısı belirsiz olan durumlar için kullanılan metot örneği

def Hesapla(*sayilar): #İstediğin kadar parametre alabilir * ile.
    toplam = 0

    for i in sayilar :
        toplam+=i

    return toplam


result = Hesapla(1,2,3,4,5,6,7,8,9)
print(result)