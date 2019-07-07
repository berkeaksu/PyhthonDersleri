#Şifrenin 3 defa yanlış girilmesi durumunda kullanıcıyı uyaran uygulama

#password = "abc123"
#fail_count = 0
#for i in range(3):
#    password_user = input("Şifrenizi giriniz : ")
#    if (password==password_user):
#        print("Giriş Sağlandı")
#        break
#    else:
#        print("Hatalı şifre girdiniz.")
#        fail_count+=1

#        if(fail_count==3):
#            print("Şifrenizi 3 kez hatalı girdiniz. Hesabınız bloke edilmiştir.")
#            break


from builtins import print

for i in range(3):
    parola = input("Şifrenizi giriniz : ")
    if i == 2 :
        print("Şifrenizi 3 defa yanlış girdiniz.")
    elif not parola :
        print("Parola boş geçilemez !!")
    elif len(parola) in range(3,8):
        print("Parolanız : ",parola,"olarak belirlenmiştir!")
        break
    else:
        print("WTF")