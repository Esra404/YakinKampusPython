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
ucus2=Ucus('TKK123','IST','ANK',60,300,50)
print(ucus2.havayolu)