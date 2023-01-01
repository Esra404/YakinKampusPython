#dogstring kodun okunabilirliğini sağlıyor """ersa""" 
def bes_bastır():
    print(5)

print(bes_bastır())
#print bastırırken return döndürür
def bes_dondur():
    return 4
print(bes_dondur())


def sayi_dondur(sayi):
    return sayi
print(sayi_dondur(100))


b=bes_dondur()
print(b)


def sayi_dondurr(sayi=250):
    return sayi

print(sayi_dondurr(1000))

def buyuk_sayi_dondur(a,b):
    if a>b:
        return a
    elif b>a:
        return b
print(buyuk_sayi_dondur(5,10))

def metin_yazdir(a,b):
    buyuk_sayi=buyuk_sayi_dondur(a,b)
    sablon_metin="{} daha buyuk sayidir".format(buyuk_sayi)
    print(sablon_metin)
print(metin_yazdir(5,10)) 

def isim_soyisim_ayirma(isim_soyisim):
    isim=isim_soyisim.split()[0]
    soyisim=isim_soyisim.split()[1]
    return isim ,soyisim
print(isim_soyisim_ayirma("gökçe gün"))
# birleştirme join metodu ile olur
# """.join(["gokce","gun"])
def isim_soyisim_birlestir(isim,soyisim):
    return "".join([isim,soyisim])
print(isim_soyisim_birlestir("oguzcan","bozkurt"))
# *args ile arguman sayısı sınırsız olabilir
def isim_soyisim_birlestir(*args):
    return " ".join(args)
print(isim_soyisim_birlestir("oguzcan","bozkurt","erol"))

# **kwargs buda ardan seçme argümanı olarak değerlendirilebilir
def gobek_adi_yazdir(**kwargs):
    if 'gobekadi' in kwargs:
        print(kwargs['gobekadi'])
    else:
        print("gobekadi yok")
print(gobek_adi_yazdir(adi="esra",soyadi="durmaz",gobekadi="derya"))
#  map lambda fonksiyonları------------------------------------------------------------------------------------------------------
# map listenin her elemanına aynı fonksiyonu uygulamamızı sağlıyor
def karesini_al(x):
    return x **2
print(karesini_al(5))
# -------------------------------------------------------------------------------------------------------------------------------------------
sayilar=[*range(1,6)]
print(sayilar)
sayilar=[*range(1,6)]
print(sayilar)
for index in range(len(sayilar)):
    sayilar[index]=karesini_al(sayilar[index])
print(sayilar)


sayilar=[*range(1,6)]
print([*map(karesini_al,sayilar)])

def cif_sayı_kareal(x):
  if x%2==0:
    return x**2
print(cif_sayı_kareal(4))
# filter-------------------------
sayilar=[*range(1,6)]
print([*filter(cif_sayı_kareal,sayilar)])

# lamda yol üstünde foksiyon kurmamız yarar
sayilar=[*range(1,6)]
print([*map(lambda x: x**2,sayilar)])

sayilar=[*range(1,6)]
print([*filter(lambda x: x if x%2 ==0 else None,sayilar)])