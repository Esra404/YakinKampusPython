# import komutu dışardan kütüphane yada modül kullanırken kullanılan bir yapıdır
import os
# os navigasyon ve içerik listeleme
print(os.getcwd())#çalışmakta olduğumuz klasörün halihazırda adresi
# mevcut klasörün altındaki dosyaları basar

print(os.listdir())
#herhangi bir klasörün altındakini merak edersem bu şekilde
print(os.listdir('/home'))
#klasörler arası geçiş yapılabiliyor şu şekilde
#os.chdir()#komutu ile
dosyalar=os.listdir()
for eleman in dosyalar:
    print(eleman+'mesut')#yeni isim verip döngüye aktarabilme
os.mkdir("/home/monica/Masaüstü/Egitim/Yakın KampusPython/dosya_gezinöe.py/esra")
print(os.listdir())
# mkdir komutu ile klasör oluşturulu
# rmdir komutu dosyayı siler
os.rmdir('/home/monica/Masaüstü/Egitim/Yakın KampusPython/dosya_gezinöe.py/esra')
print(os.listdir())