import ssl
import smtplib
kullanici ='kibarfeyzo669@gmail.com'
sifre='tuzak1212'
alici=kullanici
#baslik 'python gonderisi'
mesaj='deneme mesajı'
context=ssl.create_default_context()
port=465
host="smtp.gmail.com"
eposta_sunucu=smtplib.SMTP_SSL(host=host,port=port,context=context)
eposta_sunucu.login(kullanici,sifre)
eposta_sunucu.sendmail(kullanici,alici,mesaj)
from imap_tools import MailBox
posta_kutusu=MailBox('imap.gmail.com')
posta_kutusu.login(kullanici,sifre,initial_folde="INBOX")

import datetime
from imap_tools import AND
kriter=AND(date_gte=datetime.date(2021,1,1),from_=kullanici)
for msg in posta_kutusu.fetch(kriter):
    print(msg.text)