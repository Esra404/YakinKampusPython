#round() yuvalama işlemi için kulanılır.
# dene eğer çalışmaz ise try and except
# hatayı patlatmandan evirip çevirip gösterme gibi düşünebilirim:kodun tamamen durmamamsı için
# def tam_sayiya_cevir():
#     girdi=input("bir ondalık sayı giriniz:")
#     print("yuvalama işleminin sonucu:{}".format(round(float(girdi))))
# print(tam_sayiya_cevir())


# def tam_sayıya_cevir():
#   girdi=input("bir ondalık sayı giriniz:")
#   status=''
#   try:
#         girdi=float(girdi)
#         print("yuvalama işleminin sonucu:{}".format(round(girdi)))
#         status='basarılı'
#   except:
#         status='basarısız'
#         print("{} girdisi ondalık tipe cevirilemiyor".format(girdi))

# # finally en nihayetinde muhhakkak kullanılması gereken kısım olarak düşünebilirsin
#   finally:
#          print('tam sayıya cevirme işlemi {} olarak tamamlandı!'.format(status))
# print(tam_sayıya_cevir())


# def tam_sayıya_cevir_dongu():
#  while True:
#   girdi=input("bir ondalık sayı giriniz:")
 
#   try:
#         girdi=float(girdi)
#         print("yuvalama işleminin sonucu:{}".format(round(girdi)))
#         break
#   except:
       
#         print("{} girdisi ondalık tipe cevirilemiyor".format(girdi))
#         pass
# # finally en nihayetinde muhhakkak kullanılması gereken kısım olarak düşünebilirsin
  
# print(tam_sayıya_cevir_dongu())


try:
    4+'a'
except:
    print("girilen değerle le işlem yapılamıyor")