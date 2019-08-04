import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

myDb = myClient["PhoneBook"]
myCollection = myDb["People"]

person = {
    "FirstName" : "Murat",
    "LastName"  : "Vuranok",
    "Phone"     : "+90(532) 352 09 97",
    "Mail"      : "murat.vuranok@bilgeadam.com"
}

#'''

class Person:
    FirstName = ""
    LastName  = ""
    Phone     = ""
    Mail      = ""

    def __str__(self):
        return "{} {}".format(self.FirstName,self.LastName)

persons = {}

def AddPerson() :
    kisi = Person()

    kisi.FirstName = input("Lütfen İsim Giriniz : ")
    kisi.LastName  = input("Lütfen Soyisim Giriniz : ")
    kisi.Phone     = input("Lütfen Telefon Giriniz : ")
    kisi.Mail      = input("Lütfen Mail Giriniz : ")

    persons["FirstName"] = kisi.FirstName
    persons["LastName"] = kisi.LastName
    persons["Phone"] = kisi.Phone
    persons["Mail"] = kisi.Mail

    myCollection.insert_one(persons)
    print("Kişi Rehbere Eklendi !")
    
 #'''           


#result = myCollection.insert_one(person) // Bir kere yekledikten sonra yorum satırına aldık.

#print(myClient.list_database_names())


#'''
go_on = True

people = myCollection.find({}, {"_id" : 0})
for i in people:
    print("-"*45)
    for x,y in i.items():
        print("{} : {}".format(x,y))

while go_on:
    print("-"*45)
    print("Kisi eklemek istiyor musunuz ?")
    string = input("Y/N : ").lower()
    if (string == "y"): 
        AddPerson()
        
    else:
        go_on = False
#'''

people = myCollection.find({}, {"_id" : 0})
for i in people:
    print("-"*45)
    for x,y in i.items():
        print("{} : {}".format(x,y))
