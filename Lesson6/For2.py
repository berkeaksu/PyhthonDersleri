sehirler = ["Adana","Ankara","Ardahan","Amasya","Edirne"]

#Dizi içerisinde yer alan elemanarlın M harfi bulunanların yazdırılması.

for sehir in sehirler:
    if "m" in sehir:
        print(sehir)
    else:
        print(sehir, "ismi içerisinde \"m\" harfi geçmemektedir.")