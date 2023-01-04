import  datetime
from datetime import date
bugun=date.today()
print(bugun)
dun=date(2020,10,20)
print(dun)
bugun - dun
print(datetime.timedelta(days=1))
zaman_araligi=bugun - dun
print(zaman_araligi.days)
yarin=bugun+datetime.timedelta(days=1)
print(yarin)
from datetime import time
zaman=time(21,23,3)
print(zaman)
print(zaman.hour)
print(zaman.microsecond)
print(zaman.minute)
dt=datetime.datetime(2020,10,1,11,2,3)
print(dt.hour)
import time 
print(time.time())
baslangıc_zamanı=time.time()
print("baslama zamanı {}".format(baslangıc_zamanı))
time.sleep(4)
bitis_zamanı=time.time()
print("bitis zamanı {}".format(bitis_zamanı))
print("calısma süresi{}".format(bitis_zamanı - baslangıc_zamanı))