
def yasHesapla(dogumYili):
    return 2019 - dogumYili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)

print(ageCinar, ageAda, ageSena)










def EmekliligeKacYilKaldi(dogumYili, isim):   
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')

EmekliligeKacYilKaldi(1983, 'Ali')
EmekliligeKacYilKaldi(1950, 'Ahmet')
EmekliligeKacYilKaldi(1974, 'Yağmur')