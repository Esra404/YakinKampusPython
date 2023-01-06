import requests
grafik_URL='http://image-charts.com/chart'
payload={
    'chs':'700*190',
    'chd':'t:60,40',
    'cht':'p3',
    'chl':'Hello|World',
    'chan':None,
    'chf':'ps0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1'

}
response=requests.post(grafik_URL,data=payload)
print(response.status_code)
print(response.content)
# https://image-charts.com/chart?chs=700x190&chd=t:60,40&cht=p3&chl=Hello%7CWorld&chan&chf

print(type(response.content))
from PIL import Image
from io import BytesIO
image=Image.open(BytesIO(response.content))
print(image.show())
# RADAR
grafik_URL='https://image-charts.com/chart'
payload={
    'chco':'3092de',
    'chd':'t:81,65,50,67,59,81',
    'ch1':'hiz|sut|pas|top_surus|defans|fizik'
    'chd1''Falcao',
    'chdlp':'b',
    'chs':'480*480',
    'cht':'r',
    'chtt':'Futbolcu özellikleri'
    }
response=requests.post(grafik_URL,data=payload)
image=Image.open(BytesIO(response.contect))
print(image.show())
class Futbolcu():
    def __init__(self,isim,hiz,sut,pas,top_surme,defans,fizik):
        self.isim=isim
        self.hiz=hiz
        self.sut=sut
        self.pas=pas
        self.top_surme=top_surme
        self.defans=defans
        self.fizik=fizik
    def yetenek_hazırle(self):
        return ','.join([
            str(self.isim),
            str(self.hiz),
            str(self.sut),
            str(self.pas),
            str(self.top_surme),
            str(self.defans),
            str(self.fizik)
        ])
        
    def yetenek_gorsellestir(self):
        grafik_URL='https://image-charts.com/chart'
        payload={
        'chco':'3092de',
        'chd':'t:'+self.yetenek_hazirla(),
        'chd1':self.isim,
        'chdlp':'b',
        'chs':'480*480',
        'cht':'r',
        'chtt':'Futbolcu özellikleri',
        'ch1':'hiz|sut|pas|top_surus|defans|fizik',
        'chx1':'0:|0|20|40|60|80|100',
        'chxt':'x',
        'chxr':'0,0.0,100.0',
        'chm':'B,AAAAABB,0,0,0'
        
        
    }
    response=requests.post(grafik_URL,data=payload)
    image=Image.open(BytesIO(response.content))
    print(image.show())
    def yetenek_kiyaslama_goster(self,hedef_futbolcu):
        grafik_URL='https://image-charts.com/chart'
        payload={
        'chco':'3092de,027182',
        'chd':'t:'+self.yetenek_hazirla()+'|'+hedef_futbolcu.yetenek_hazırla(),
        'chd1':self.isim +'|'+hedef_futbolcu.isim,
        'chdlp':'b',
        'chs':'480*480',
        'cht':'r',
        'chtt':'Futbolcu özellikleri',
        'ch1':'hiz|sut|pas|top_surus|defans|fizik',
        'chx1':'0:|0|20|40|60|80|100',
        'chxt':'x',
        'chxr':'0,0.0,100.0',
        'chm':'B,AAAAABB,0,0,0|B,0073CFBB,1,0,0'
        }
     







messi=Futbolcu('messi',85,92,91,95,38,65)
ronaldo=Futbolcu('Robaldı',89,93,81,89,35,77)
print(messi.yetenek_gorsellestir())
print(messi.yetenek_kiyaslama_goster(ronaldo))