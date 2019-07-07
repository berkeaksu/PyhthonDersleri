
# Dısarıdan girilen metin içerisinde yer alan tüm karakterlerin ASCII kod değerlerinin vapurda bulunuz


def ASCII_Toplam(string):
    toplam = 0
    counteri = 0
    for i in range (len(string)):

        if " " in string :
            string.remove(" ")
            print(string)
    myList = string

    for i in range(len(myList)):
        n = ord(myList[i])
        #print(n)
        n = int(n)
        toplam = toplam + n


    return toplam

string = list(input('Bir metin giriniz : '))



print(ASCII_Toplam(string))


#---------------------------------------------------------------------------------------------------------------------


