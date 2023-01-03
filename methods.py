class Ucus():
   havayolu="THY"
#    ucus1=Ucus()
#    print(ucus1.havayolu)
   def __init__(self, kod, kalkis,varis,sure,kapasite,yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu
   def anons_yap(self):
        return "{} sefer sayili {}-{} ucuusumuz {} dakika sürecektir".format(
        self.kod,
        self.kalkis,
        self.varis,
        self.sure)
   def koltuk_sayisi_guncelle(self):
        return self.kapasite-self.yolcu
   def bilet_satisi(self,bilet_adedi=1):
    if self.yolcu + bilet_adedi<=self.kapasite:
        self.yolcu +=bilet_adedi
        self.koltuk_sayisi_guncelle()
        print('{} adet bilet satilmistir,kalan koltuk sayisi{}'.format(
            bilet_adedi,
            self.koltuk_sayisi_guncelle()
        ))
    else:
        print('islem gerçekleştirilemedi yetersiz koltuk sayısı')
   def bilet_iptal(self,bilet_adedi=1):
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi
            print('{} adet bilet iptal edilmiştir,güncel koltuk satisi{}'.format(
                bilet_adedi,
                self.koltuk_sayisi_guncelle()
            ))
        else:
            print('islem gerçekleştirilemedi iptal edilecek kadar koltuk sayisi yok')



ucus3=Ucus('TKK122','BOD','ANT',45,350,300)
# print(ucus3.koltuk_sayisi_guncelle())
print(ucus3.bilet_satisi(5))
print(ucus3.bilet_satisi(5))
# print(ucus3.bilet_satisi(50))
print(ucus3.koltuk_sayisi_guncelle())
print(ucus3.bilet_iptal(400))