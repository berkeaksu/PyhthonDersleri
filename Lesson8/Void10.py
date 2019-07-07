# Odev, dısarıdan aldığı degere gore bos kare cizen metot

def IcıBos_Kare(b):

    kare1 = 0
    kare2 = b-1
    counteri = 0

    for i in range(b):
        for j in range(b):
            if i == kare1 or i == kare2 or j == kare1 or j ==kare2 :
                print("x", end = "  ")
            else:
                print(" ", end = "  ")
        print()


kare = int(input("Kare büyüklüğünü giriniz : "))

IcıBos_Kare(kare)