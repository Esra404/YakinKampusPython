# yorum_birakanlar=["esra","ali","derya"]
# for kullanici in yorum_birakanlar:
#     print(kullanici)

# kullanici_sayisi=0
# yorum_birakanlar=["esra","ali","derya"]
# for kullanici in yorum_birakanlar:
#     kullanici_sayisi=kullanici_sayisi+1
#     print(kullanici_sayisi, kullanici)
#     #split metodu boşuk varsa olayı ikiye bölüyordu
# print(yorum_birakanlar[0].split())

#------------------------------------------------------------------
# kullanici_sayisi=0
# for kullanici in yorum_birakanlar:
#     kullanici_sayisi=kullanici_sayisi+1
#     ad,soyad=kullanici_sayisi.split()[0],kullanici.split()[1]
#     print('{0}.kulllanıcının adı {1} ve soyadı {2}'.format(kullanici_sayisi,ad,soyad))
# tup1 =(1,3,5,7)
# for sayi in tup1:
#         print(sayi)

# liste =[[1,3],[3,4]]
# for x,y in liste:
#     print(x,y)


# liste =[[1,3],[3,4],[5,6]]
# for x,y in liste:
#     print(x*y)


# kullanici1={
#     'ad':'esra',
#     'soyad':'durmaz'
# }
# print(kullanici1.items())

# for k,v in kullanici1.items():
#     print("key:{} \t value:{}".format(k,v))
    # while---------------------------------------------
# x=0
# while x<10:
#     print("{}değeri ondan küçüktür".format(x))
#     x +=1
# else:
#     print("{} değeri ondan küçük değildir".format(x))
# sonuc=1
# sayi=6
# while sayi>0:
#     sonuc= sonuc*sayi
#     sayi -=1
# print(sonuc)
# range---------------
# print(range(10))
# print(list(range(10)))
# print([*range(10)])
# print([*range(2,7,2)])
# for sayi in range(10):
#     print(sayi)
# enumarete-------------------- tuple ye benxeyen yapı hem ona gelen karşılığı hemde indexi gösteriyor
# harfler=['a','b','c','d','e']
# for harf in enumerate(harfler):
#     print(harf)
# for index , harf in enumerate (harfler):
#     print("{}.harf:{}".format(index+1,harf))
#     # zip--------------------------

# ulkeler=['TR','FR','DE']
# siralamalar=range(1,4)
# for ulke in zip(ulkeler,siralamalar):
    # print(ulke)
# break ------------döngüyü kırarr
# harfler=['a','b','c','d','e']*100
# for index,harf in enumerate(harfler):
#     if harf =='c':
#         print('{} harfi {}. indexte'.format(harf,index))
#         break 
# continue--------------------DEWAMKE
for sayi in range(1,6):
    if sayi%2==0:
     continue
    print(sayi) #BAKSANA Bİ ABİ
for sayi in range(1,6):
    if sayi%2==0:
     pass
    print(sayi)


# bişeylaerr yazmak isteyip bulamadığında da pass mantığını kullanabilirsin