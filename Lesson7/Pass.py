while True:
    sifre = input("Lütfen şifre giriniz : ")
    if not sifre :
        pass
    elif len(sifre) in range (3,8):
        print("Yeni şifreniz : ",sifre)
        break
    else:
        print("Şifreniz 3 ile 8 karakter arasında olmalıdır.")

