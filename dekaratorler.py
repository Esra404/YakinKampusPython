#ambalajlama gibi düşünebilir.
def deneme():
     print("abc")
print(deneme())
f=deneme
print(f())
def deneme():
     print("deneme fonksiyonu çalışıyor")
     def test():
         return "test fonksiyonu çalışıyor"
     print(test())
print(deneme())
def deneme():
     print("deneme fonksiyonu çalışıyor")
     def test():
          return "test fonksiyonu çalışıyor"
     return test
print(deneme())
f=deneme()
print(f())
def deneme():
    return "denemee fonksiyonu çalışıyor"
def ikinci(f):
    print("ikinci fonksiyon çalışıyor")
    print(f())
ikinci(deneme)
def deco(f):
    def wrapper():
        print("başlangıç")

        f()
        print("bitis")
    return wrapper
def yazdir():
    print("yazdir")
yazdir=deco(yazdir)
print(yazdir())

# yazdir2=deco(yazdir2)
# print(yazdir2())
@deco
def yazdir():
    print("yazdir")
print(yazdir())
def deco (f):
    def wrapper(*args):
        print("başlangıç")
        f(*args)
        print("bitis")
    return wrapper
@deco
def toplama(a,b):
 print(a+b)
print(toplama(2,3))
def deco(msg1,msg2):
    def ara_katman(f):
        def wrapper(*args):#birden çok argümanı algılamıyor
            print(msg1)#ara katman olarak belirtebiliriz

            f(*args)
            print(msg2)
        return wrapper
    return ara_katman

@deco("başlama","sonuç")
def toplama(a,b):
    print(a+b)
print(toplama(4,5))
import time
baslangic=time.time()
f()
bitis=time.time()
bitis-baslangic
def sure_olc(f):
    def wrapper(*args):
        baslangic=time.time()
        print("baslangiç zamanı: {}".format(baslangic))
        f(*args)
        bitis=time.time()
        print("bitis zamanı{}".format(bitis))
        print("gecen zaman {}".format(bitis-baslangic))
    return wrapper
@sure_olc
def factoriel(sayi):
    toplam=1
    while sayi>1:
        toplsm=toplam*sayi
        sayi=sayi-1
    print(toplam)
print(factoriel(1000))