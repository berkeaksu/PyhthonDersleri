# Dısarıdan alınan metin icerisindeki turkce ve ozel karakterleri replace metotu kullanmadan değiştiren metot yazımı


def Replace(string)->str:

    isReplacable = {
        "ğ" : "g",
        "ç" : "c",
        "ş" : "s",
        "ü" : "u",
        "ö" : "o",
        "ı" : "i",
        "Ğ" : "G",
        "Ç" : "C",
        "Ş" : "S",
        "Ü" : "U",
        "Ö" : "O",
        "İ" : "I",
        "§" : ".",
        "~" : ".",
        "€" : "."

    }

    for i in range (len(string)):

        if string[i] in isReplacable:
            element = string[i]
            n = isReplacable[string[i]]
            string.remove(element)
            string.insert(i,n)




    return ''.join(string)



string = input("Lütfen bir metin giriniz : ")
string=list(string)

print(Replace(string))