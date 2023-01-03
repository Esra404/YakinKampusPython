# def sayi_girdisi_kontrol():
#     girdi=input("bir sayı giriniz:")
#     if girdi.isdigit():
#         print("tebrikler !Sayı tipi değer girdiniz....")
#     else:
#         print("üzgünüz. bu bir sayı tipi değişken değildir..")
# print(sayi_girdisi_kontrol())


def sayi_girdisi_kontrol():
    girdi=input("bir sayı gşrşniz=")


    while not girdi.isdigit():
        print("üzgünüm bu bir sayı tipi değişken değildir.")
        girdi=input("bir sayı giriniz= ") 


    else:
        print("tebrikler sayı tipi değişken girdiniz.")
print(sayi_girdisi_kontrol())