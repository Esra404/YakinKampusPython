kullanici1 = {
    'ad': 'Ferhat',
    'soyad': 'Ibrik',
    'uzmanlik': ['Front-End']
}
kullanici2 = {
    'ad': 'Gokce',
    'soyad': 'Gün',
    'uzmanlik': ['Tasarim']
}
kullanici3 = {
    'ad': 'Mesut',
    'soyad': 'Gün',
    'uzmanlik': ['Front-End']
}
# Soru 1: Ferhat Ibrik Kullanicisinin uzmanlik alanlarini döndür

print(kullanici1['uzmanlik'])
# ['Front-End']
kullanici_listesi = [kullanici1, kullanici2, kullanici3] 
for kullanici in kullanici_listesi:
    if 'Front-End' in kullanici.get('uzmanlik'):
        print(kullanici.get('ad'))

# Soru 2: Front-end alanindaki uzmanlarin isimlerini döndür

# Ferhat
# Mesut
# Soru 3: Mesut kullanicisi Yazilim ögrendi, bilgileri güncelle!
[{'ad': 'Ferhat', 'soyad': 'Ibrik', 'uzmanlik': ['Front-End']}, {'ad': 'Gokce', 'soyad': 'Gün', 'uzmanlik': ['Tasarim']}, {'ad': 'Mesut', 'soyad': 'Gün', 'uzmanlik': ['Front-End', 'Yazilim', 'Yazilim']}]
# Soru 4: 1den fazla uzmanlik alani olan kullanicilari döndür (Hint: length)
{'ad': 'Mesut', 'soyad': 'Gün', 'uzmanlik': ['Front-End', 'Yazilim', 'Yazilim']}
kullanici_yaslari_listesi = [22, 34, 32]
# Soru 5: zip kullanarak iki listeyi birlestir ve yasi 30'dan az olan kullanicilar kimler?
{'ad': 'Ferhat', 'soyad': 'Ibrik', 'uzmanlik': ['Front-End']}
# Soru 6: deger isimli degiskene atanan sayinin asal olup olmadigini söyle!
# Hint Asal sayi: kendinden ve 1'den baska böleni olmayan sayilar örnek 2,3,5,7

deger = 3
# 3 sayisi asaldir!