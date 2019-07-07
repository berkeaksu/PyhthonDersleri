# 1 ile bin arasında yer alan tek ve çift sayıların adedini ekrana yazdırınız.

sayi = 1
cift_counter = 0
tek_counter = 0
while sayi <= 1000 :

    if(sayi%2==0):

        cift_counter += 1

    else:

        tek_counter += 1

    sayi += 1

print("Çift Sayı Adedi : ",cift_counter)
print("Tek Sayı Adedi : ",tek_counter)