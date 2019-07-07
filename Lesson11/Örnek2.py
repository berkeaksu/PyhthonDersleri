file1 = "ba.png"
file2 = "ba.jpg"
file3 = "ba.gif"
file4 = "ba.png"
file5 = "ba.tff"
file6 = "ba.mp3"
file7 = "ba.mp4"
file8 = "ba.jpg"
file9 = "ba.gif"
file10 = "ba.png"
file11 = "ba.gif"

# Yukarıda yer alan dosyalar içerisinde .png olanların sayısını ekrana yazdırınız.

def SeekPNG(a):
    toplam = 0
    for i in fileList:

        if i.endswith(".png"):
            toplam +=1

    return toplam


fileList = [file1,file2,file3,file4,file5,file6,file7,file8,file9,file10,file11]

print(SeekPNG(fileList))