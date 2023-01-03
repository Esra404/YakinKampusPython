def eposta_kontrol():
    girdi =input("Geçerli bir e posta adresi giriniz")

    while not (('.'in girdi) and ('@' in girdi)):
        print("Üzgünüzm! bu geçerli bir e posta adresi değildir..")
        girdi=input("geçerli bir e posta adresi girdiniz:")

    else:
        print("tebrikler.. e posta adresinize başarıyla giriş yaptınız...")   
print(eposta_kontrol())