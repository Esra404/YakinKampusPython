a=True
b=False
print(a)
print(b)
print(type(a))
print(type(b))
c='true'
print(c)
print(type(c))
#koleksiyon veri tipleri
#listeleme ve set
liste=['a','b','c']
liste=liste+['f']#liste ye anca liste ekleyince bir sonuç çıkabilit
print(liste)
print(liste[1:4])
liste.append('g')
print(liste)
liste.pop(4)
print(liste)
sayilar=[252362,23132,3,3,4433,344]
sayilar.sort()
print(sayilar)
sayilar.reverse()
print(sayilar)
set(sayilar)#tekrarlama işlemini ortadan ,kaldırır set ile çağırınca
#süslü pantezler kullanılır set te
#tuple
liste=['a','b','g','l','f']
print(liste)
tup=('a','b','g','l','f','a')
print(tup)
liste[0]=1212
print(liste)#tuo ifadeler değer atamasını karşlamaz
print(tup)
print(tup.count('b'))#burada ise hem birin hem sıfırın karşılığı bulunmakta
print(tup.index('a'))#indexte bir karşılığı varken sıfırın karşılığı bulunmuyor
#dictionary
dict1={'isim':'mesut','yas':32,'lokasyon':'berlin'}
print(dict1)
dict
