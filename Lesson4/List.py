# Tanımlama şekli
# Bir dizinin maksimum index değeri, eleman sayısının bir eksi değeridir.
sehirler = ["ankara","edirne","eskisehir","istanbul","kars","kayseri","istanbul"] #List
         # eleman sıra no : 1,2,3,4,5,6,7
         # eleman index no : 0,1,2,3,4,5,6

print(sehirler[0])
index = len(sehirler)-1
print(sehirler[index])

print(sehirler[0:4]) # 1. paramatre index değeri, 2.parametre ise verilen index değerinin bir alt değerine kadar yazdırır

print(sehirler[:])
