# Dictionary key value formatında listelemek için kullanılır. Json formatında data tutar. MongoDB, WebApi(servisler), JavaScript(Vue Js, Angular Js, Angular IO, React, React-Native, Cordova vs) gibi bir çok platfor bunu destekler.

personeller = [
    {
        "ID" : 1,
        "FirstName" : "Ahmet Berke",
        "LastName" : "Aksu"
    },
    {
        "ID": 2,
        "FirstName": "Göker",
        "LastName": "Çengel"
    },
    {
        "ID": 3,
        "FirstName": "Ali Nejat",
        "LastName": "Develi"
    }
]


print(personeller[0])

# dizi içerisinde eğer bir index içerisindeki elemanın herhangi bir property'sini ekrana yazdırmak

print(personeller[0]["FirstName"])

#----------------------------------------------------------------------------------------------------------

# Liste içerisinde yer alan bir elemanın güncellenmesi

guncellenecekIndex = 2
guncellenecekKey = "FirstName"

oldName = personeller[guncellenecekIndex][guncellenecekKey]

personeller[guncellenecekIndex][guncellenecekKey] = "Okan"
print(oldName, "Adlı, Personelin Adı : ", personeller[2]["FirstName"], "olarak güncellenmiştir.")

#----------------------------------------------------------------------------------------------------------

# Diziye yeni bir kayıt ekleme


personeller.append({"ID" : 4, "FirstName" : "Kaplan Uğur", "LastName" : "Bulut"})

print(personeller[3])
print("Eklenen Personelin Adı : {}\nEklenen Personelin Soyadı : {}".format(personeller[3]["FirstName"],personeller[3]["LastName"]))

# .format içerisindeki parametrenin ilk değeri 0'dır. Place Holder içerisinde index belirtilmez ise default olarak "0,1,2" olarak devam eder.
# Place Holder içerisine istenilen şekilde index değeri girilebilir. Sıralı olması gerekmez.

#----------------------------------------------------------------------------------------------------------

