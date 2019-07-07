#Dısarıdan girilen sayının karakterlerinin birbiri ile toplamı :

index = 0
sayi = input("Bir sayi giriniz : ")
toplam = 0
while index < len(sayi):
    toplam = toplam +(int(sayi[index]))
    index+=1

print(toplam)