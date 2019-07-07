# Kullanıcı dısarıdan string olarak sayı dizisi gönderecek

# Gelen string değeri geriye sayılsal bir dizi olarak döndürünüz :




def ConvertToList(a):

    myList = a.split()
    print(myList)

    for n in range(len(myList)):

        if myList[n].count(".") :
            myList[n] = float(myList[n])
        else:
            myList[n] = int(myList[n])

    return myList

print(ConvertToList("3 1 0 25 46.5 87.9 27 66 77 93.5 "))

deger = input("Deger giriniz : ")

print(ConvertToList(deger))


