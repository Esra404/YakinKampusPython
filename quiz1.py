# # 3 ve 2'yi toplamı için bu alanı kullanabilirsin:
print(3+2)
# print(3+2)
# 5
# # 5 ve 4'ü çarpımı için bu alanı kullanabilirsin:
print(5*4)
# # 5 ve 4'ün bölümünden kalan için bu alanı kullanabilirsin:
print(5%4)
# Aşağıdaki hücreleri kullanarak, şu işlemleri yanıtlandır:

# # 2.3 ve 4.7'nin toplama işleminin neticesi hangi veri tipindedir?
# int float
# dict 
# dict
# # 2.3 ve 4.7'nin toplama işleminin veri tipini, komut kullanarak ekrana bastır?
# print(type(2.3+4.7))
# ---------------------------------------------------------------------------------
strvar = 'Yakın Kampüs'
# Yukarıdaki değişkeni kullanarak, aşağıdaki hücrelerde, şu işlemleri yanıtlandır:

# # "ü" harfini index komutu kullanmadan döndür (İpucu: [])
print(strvar[10])
print(strvar.index('ü'))
# # "ü" harfinin konumunu, index komutu kullanarak döndür
# # strvar.upper().lower() ifadesinin cevabi nedir?
print(strvar.upper())
print(strvar.lower())
print(strvar.upper().lower())
# # split() komutunu boşluk(space) dışında başka bir parametre ile kullan.
print(strvar.split('k'))
# Boolean
a = True
b = False
c = 'True'
# Yukarıdaki değişkenleri kullanarak, aşağıdaki hücrelerde, şu işlemleri yanıtlandır:

# # a == b sorgusu cevap olarak ne döndürür?
print(a==b)
# # a == c sorgusu cevap olarak ne döndürür?
print(a==c)
# # a!=b sorgusu cevap olarak ne döndürür?
print(a!=b)
# # ! ve not hangi senaryoda birbirinin yerine kullanilamaz? (İpucu: >)
# # # > ya da < isareti ile ! ayni anda kullanilamaz, ama not ifadesi kullanilabilir
# # type(3) == type('3') sorgusunu cevap olarak ne döndürür?
type(3) == type('3')
# Listeler ve Setler
liste = [1, 'a', 2, 3, True, 4, 5, 'True', '1']
# Yukarıdaki değişkeni kullanarak, aşağıdaki hücrelerde, şu işlemleri yanıtlandır:

# # Listenin son elemanını nasıl bulabiliriz?
print(liste.pop())
# # Listenin 2. ve 4. elemanlarını içeren yeni bir liste oluştur (İpucu [::])
print(liste[2:5:2])
# # Listeyi metod kullanarak nasıl ters sıralarsınız?
print(liste.reverse())
# # Listeyi [::] kullanarak nasıl ters sıralarsınız?
print(liste[7:-7:-1])
# # Eğer yukarıdaki listeyi, set'e çevirecek olsak eleman sayısı farklı olur muydu? Neden?
# #
print(set(liste))
ic_ice_liste = [1,2,3,[4,5]]
# Yukarıdaki değişkeni kullanarak, aşağıdaki hücrelerde, şu işlemleri yanıtlandır:

# # 5 değerine nasıl ulaşırsınız?
# print(ic_ice_liste([3][-1]))
# #  ic_ice_liste değişkeninin son konumunda bulunan elemanını listeden atın ve bu kısmı bir degişkene atayın
ic_ice_liste.pop(3)
print(ic_ice_liste)
yeni=ic_ice_liste+[49,8]
print(yeni)
yeni.pop(4)
print(yeni)
yeni.pop(3)
print(yeni)
yeni+=[[4,5]]
print(yeni)
# #  pop komutunu kullanmayarak listeyi nasil [1,2,[4,5]] sekline cevirebilirsiniz? (Hint: her yol mübah :D )

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Dictionary
# Dictionary veri tipinin listeden farkı nedir?
# her türlü farlı yapıyı tutuyor
# Dictionary oluştururken kullanılan anahtar ve değer çiftinin Python'daki karşılıkları nelerdir?
#--key,--value
my_dict = {'isim': 'Mesut', 'yas':32, 'lokasyon': {'yasadigi':'Berlin', 'dogdugu': 'Istanbul'}}
# 32 değerine nasıl ulaşırsınız?
print(my_dict['yas'])
# isim anahtarına karşılık gelen değeri, kendi isminizle değiştirin:
my_dict['isim']='esra'
print(my_dict)
# my_dict değişkenindeki 'Istanbul' değerine nasıl ulaşabiliriz?
print(my_dict['lokasyon']['dogdugu'])
# my_dict değişkenindeki bütün anahtar değerlerine nasıl ulaşırız?
print(my_dict.keys())
# Tuple
# Tuple ile liste arasındaki farklar nelerdir?
#tuple bir değeri bir edfa kullanılır ve değiştirilmez o değerler İMMUTABLE
# # Genel Konular
# print komutu ile ve print komutsuz yazdırmanın farkı nedir? Her durumda birbiri yerine kullanılabilir mi?
#Bİİ EKRANA BASARKENDİĞERİ EKRANA BASMAZ
# String ifadelerinin içerisinde \t ile \n kullanmanın farkı nedir?
#biri bir tab boşluğu bırakırken diğeri diğeri alt satra geçmemizi sağlar
# değişken isimlendirmelerinde dikkat edilmesi gereken hususlar nelerdir?
#camel case önemlidir
# [] {} ve () işaretlerini veri tipleri ile eşleştirin:
# '' -> String 
# [] -> liste
# {} -> dictionary
# () ->tuple,ser