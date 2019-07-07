# Metot (Ad, Soyad, Telefon, Gorev)
# Metot (*parametreler):


def Metot(Ad, Soyad, Telefon, Gorev, *par):
    print(Ad,Soyad,Telefon,Gorev, *par)


def Metot1 (*params):
    print(params)
    for i in params :
        print(i)


Metot("murat","vuranok","6526848646","Danışman", 3265,484,3221,848,458)
Metot1("murat","vuranok","6526848646","Danışman")

# murat vuranok 6526848646 Danışman
# murat
# vuranok
# 6526848646
# Danışman


def MetotVol1(**params):
    print(params)

MetotVol1(Ad = "Murat", Soyad = "Vuranok", Telefon = "2661532", Mail = "murat.vuranok@bilgeadam.com")

# {'Ad': 'Murat', 'Soyad': 'Vuranok', 'Telefon': '2661532', 'Mail': 'murat.vuranok@bilgeadam.com'}

def MetotVol2(**params):
    print(params["Ad"])

MetotVol2(Ad = "Murat", Soyad = "Vuranok", Telefon = "2661532", Mail = "murat.vuranok@bilgeadam.com")

# Murat