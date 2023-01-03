# girdi=input("lütfen bir sayı gir ")
# print(girdi)
# print(type(girdi)) 
def uygulama():
    girdi=input("bir sayı giriniz :")
    islem=input("verinin çift mi tek mi olduğunu sorgula :")

    if islem =='cift':
        if int(girdi)%2==0:
            return 'evet {} sayısı  bir cift sayıdır '.format(girdi)
        else:
            return 'hayır {} sayısı  cift sayi değildir '.format(girdi)
    elif islem == 'tek':
        if int(girdi)%2==1:
            return 'evet {} sayısı  bir tek sayıdır '.format(girdi)
        else:
            return 'hayır {} sayısı  bir tek sayı değidir '.format(girdi)
print(uygulama())