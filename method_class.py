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
ucus3=Ucus('TKK122','BOD','ANT',45,350,350)
print(ucus3.anons_yap())
