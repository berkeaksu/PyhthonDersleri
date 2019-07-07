from random import randint

#print(randint(1,50)) #max 49, min 1 değerini üretir.

# Rastgele 6 adet sayı üretip bunu bir diziye ekleyin. Eğer aynı sayı dizi içerisinde geçiyor ise tekrar üretin.

sayilar = []
temp = []

counter_i = 0

i = 0
while i<6:
    i+=1
    sayi = randint(1, 50)
    #temp.append(sayi)
    #print("Temp : ", temp)
    if sayilar.count(sayi):
        i-=1

    else:
        sayilar.append(sayi)

        #counter_i +=1

sayilar.sort()
print("Sayi Dizisi : " ,sayilar)