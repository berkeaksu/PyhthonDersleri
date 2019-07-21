from Muzisyen import Muzisyen
from Bateri import Bateri
from Gitar import Gitar

gitar = Gitar()
gitar.Marka = "Yamaha"
gitar.Aciklama = "Pahalı"
sound = gitar.Cal()

muzisyen = Muzisyen()
muzisyen.Adi = "Berke"
muzisyen.Soyadi = "Aksu"
muzisyen.Enstruman = gitar


result = """
Adı            : {}
Soyadı         : {}
Enstruman Sesi : {}
Marka          : {}
Açıklama       : {}
""".format(muzisyen.Adi,muzisyen.Soyadi,sound,muzisyen.Enstruman.Marka,muzisyen.Enstruman.Aciklama)

print(result)