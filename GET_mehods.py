import requests
bolgeler_URL="https://data.police.uk/api/forces"
response=requests.get(bolgeler_URL)
print(response.status_code)
print(response.url)
print(response.json())
suc_kategorileri_URL="https://data.police.uk/api/crime-categories"
payload={'date':'2020-01'}
response =requests.get(suc_kategorileri_URL,params=payload)
print(response.status_code)
print(response.url)
print(response.json())
suc_URL='https://data.police.uk/api/crimes-no-location'
payload={
    'category':'all_crime',
    'force':'city-of-london',
    'date':'2020-01'
}
response=requests.get(suc_kategorileri_URL,params=payload)
print(response.json())
from collections import Counter
class SucRaporu():
    def __init__(self,bolge,tarih,suc_tipi='all-crime') :
     self.bolge=bolge
     self.tarih=tarih
     self.suc_tipi=suc_tipi
     self.suclar=self.sucları_bul()


    def sucları_bul(self):
        suc_URL='https://data.police.uk/api/crimes-no-location'
        payload={
            'category':self.suc_tipi,
            'force':self.bolge,
            'date':self.tarih
        }
        response=requests.get(suc_URL,params=payload)
        if response.status_code==200:
            return response.json()
        else:
            return None
    def sucları_raporla(self):
        suclar_listesi=[]
        if self.suclar is not None:
            for suc in self.suclar:
                suclar_listesi.append(suc['category'])
            return Counter(suclar_listesi)
sr=SucRaporu('norfolk','2020-02','bicycle-theft')
sr.suclari_raporla()