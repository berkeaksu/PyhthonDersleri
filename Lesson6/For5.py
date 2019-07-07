#10-20 arasındaki asal sayıları ekrana yazdır.



for i in range(10,21): # 20'yi de dahil ettik.
    for bolen in range(2,i):
        if   i%bolen == 0:
            j = i / bolen
            print("{} eşittir : {}*{} ".format(i,bolen,int(j)))
            break
    else:
        print(i," asal sayıdır. ")