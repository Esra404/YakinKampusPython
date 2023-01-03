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
   def __repr__(self):
    return "{} sefer sayılı ucus,sistemde olusturulmustr...".format(self.kod)
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
print(ucus3)


class Seyahat():
    def __init__(self,kalkis,varis):
        self.kalkis=kalkis
        self.varis=varis
    def anons(self):
        return "{}-{}seahatine hoşgeldiniz".format(self.kalkis,self.varis)


class Otobus(Seyahat):
    def __init__(self, mola_durakları):
        Seyahat.__init__(self,'ist','ank')
        self.mola_durakları=mola_durakları
seyahat1=Seyahat('ANT','BOD')
print(seyahat1.anons())
oto1=Otobus(['FET','ALAN'])
print(oto1.mola_durakları)
print(oto1.kalkis)
print(oto1.anons())