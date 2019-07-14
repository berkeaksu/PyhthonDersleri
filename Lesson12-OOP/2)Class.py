class Employee :

    '''
    Personel Tanımlama
    '''

    FirstName  = ""
    LastName   = ""
    Department = ""
    Mail       = ""
    Phone      = ""

# Employee sınıfından instance(yeni bir örnek almak) alma
personel = Employee()

personel.Mail       = "murat.vuranok@bilgeadam.com"
personel.Department = "Yazılım"
personel.FirstName  = "Murat"
personel.LastName   = "Vuranok"
personel.Phone      = "54864626"

print(personel) # <__main__.Employee object at 0x00AEEB30> ----> Ram deki adresi teslim eder.
# Eğer sınıfı direkt olarak yazdırırsak bize, o sınıfın adı ve heap üzerindeki adresini teslim eder.

print(personel.LastName)