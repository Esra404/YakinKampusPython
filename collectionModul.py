from collections import Counter
import random
list1=random.sample(range(10),k=4)
list2=random.sample(range(10),k=4)
list3=random.sample(range(10),k=4)
list4=random.sample(range(10),k=4)
liste_listesi=[list1,list2,list3,list4]
list_toplam=list1+list2+list3+list4
print(liste_listesi)
print(list_toplam)
for index,liste in enumerate(liste_listesi):
    print('{}.liste \t{}'.format(index,liste))
print(Counter(list_toplam))
# Counter("adsgsvdsbcdnm")
# print(Counter)
sarki="""Yine bana gel
Yana yana yine beni sev
Yine bana gel
Yana yana yine beni sev
"""
print(Counter(sarki))
print(sarki.split())
print(Counter(sarki.split()))
sarki.lower()
print(Counter(sarki.lower().split()).most_common(2))