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
    'chd1':'Falcao',
    'chdlp':'b',
    'chs':'480*480',
    'cht':'r',
    'chtt':'Futbolcu özellikleri'
    }
response=requests.post(grafik_URL,data=payload)
image=Image.open(BytesIO(response.contect))
print(image.show())