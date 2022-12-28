# sayi=12
# print(sayi)
#değişkenler sayı ile başlayamaz isimlendirme yapılırken arada boşluk olamaz
# dictionary --dict -->sayı string herşeyi alıyor süsülü pantez kullanılır
# tuple tup değiştrilemeyen değerleri alıyor herşey alabilir
print(3*8)
# akıl karışıklığı olan bütün işlemleri sırasıyla yapar python
print(3*5.3)
# tipi otomatik olarak algılar
# STRİNG TİPİ VE CHAR TİPİ DEĞİŞKELERİ TANIMLAMA
# '',"" ŞEKLİNDE İFADE EDİLİR 

strvar="Python"
print(strvar)
strvar[2] #ikinci indexi gösterir
# [] #tek bir elelman alınır
# [:] #baslangıç ve bitiş arasındaki elemanları alır
# [::] #başlangıç ve bitiş arasındaki elemanları üçüncü kısımdaki değere göre alır
print( strvar[:3 ])
print(strvar[2:5])
print(strvar[:])
print(len(strvar))
strvar=strvar+' ogren'
print(strvar)
print(strvar*5)
print(strvar)
print(strvar.upper())
print(strvar.lower())
print(strvar.split())
print(strvar.split("o"))