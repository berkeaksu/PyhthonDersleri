# .splitlines => her bir alt satırdaki elemanların aralarına [,] karakteri ekler.
# Not : Metin altta yer alan örnekteki gibi yazıldı ise geçerlidir.

metin ="""Bilge
Adam
Beşiktaş
Yazılım
Python
Dersleri
"""

print(metin.splitlines())
#['Bilge', 'Adam', 'Beşiktaş', 'Yazılım', 'Python', 'Dersleri']

# Eğer parametre olarak sonuna True eklenirse aralarına [\n] ekler.

print(metin.splitlines(True))
#['Bilge\n', 'Adam\n', 'Beşiktaş\n', 'Yazılım\n', 'Python\n', 'Dersleri\n']