havaDurumu="karlı"
if havaDurumu =="yagıslı":
    print("semsiyeni al")
elif havaDurumu == "karlı":
    print("atkını al")
else:
    print("sen buraya ait değilsin")


yas=16
if yas>18:
    print("selam")
else:
    print("sen  uraya ait değilsin")



liste=['a','b','c']
hedef_harf='d'
if hedef_harf in liste:
    print('buldum')
else:
    liste.append(hedef_harf)
    print('liste ekledim')
    print('güncel liste {}'.format(liste))




liste=['d','b','c','a']
hedef_harf='d'
if hedef_harf in liste and (hedef_harf == liste[0]):
    print('buldum ama ilk konumda ')
elif  hedef_harf in liste :
    print('buldum ama ilk konumda değil')
else:
    liste.append(hedef_harf)
    print('liste ekledim')
    print('güncel liste {}'.format(liste))