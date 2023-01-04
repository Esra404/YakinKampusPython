import re
cumle="Mustafa Kemal Atatürk,Türk asker,devlet adamı ve Türkiye Cumhuriyetinin kurucusu"
patern="Türk"
print(re.search(patern,cumle))
durum=re.search(patern,cumle)
print(durum.span())
print(durum.start())
print(durum.end())
print(durum.group())
for eslesme in re.findall(patern,cumle):
    print(eslesme)
for eslesme in re.finditer(patern,cumle):
    print(eslesme.span(),eslesme.group())
ornek ="en sevdiğim kanal base62"
patern="base\d\d"
print(re.search(patern,ornek))