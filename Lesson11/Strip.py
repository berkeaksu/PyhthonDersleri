# .strip() => metin başındaki veya sonundaki karakteri silmek için kullanılır.

metin = " bilge adam "

print(metin)
print(len(metin))

# bilge adam
#12


metin = metin.strip(" ") #soldaki ve sağdaki boşlukları siler

print(metin)
print(len(metin))

#bilge adam
#10

metin = " bilge adam "
metin = metin.lstrip() #soldaki bpşluğu siler

print(metin)
print(len(metin))

#bilge adam
#11


metin = " bilge adam "
metin = metin.rstrip() #sağdaki bpşluğu siler

print(metin)
print(len(metin))

# bilge adam
#11