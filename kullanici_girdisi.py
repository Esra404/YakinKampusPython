def sayi_girdisi_kontrol():
    girdi=input("bir sayı giriniz:")
    if girdi.isdigit():
        print("tebrikler !Sayı tipi değer girdiniz....")
    else:
        print("üzgünüz. bu bir sayı tipi değişken değildir..")
print(sayi_girdisi_kontrol())