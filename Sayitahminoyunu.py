import random 
import time 

print("sayı tahmin oyununa hoş geldiniz \n 1-100 arasınfda bir sayı tahmin edin")
sayi = random.randint(1,100)
tahmin_hakki  = 5

while True:
    tahmin = int(input("Tahmininiz: "))
    
    if tahmin == sayi:
        print("Sayı sorhgulanıyor...")
        time.sleep(1)
        print("Tebrikler! doğru bildiniz")
        break
    elif tahmin > sayi:
        print("Sayı sorgulanıyor...")
        time.sleep(1)
        tahmin_hakki-=1
        print("Daha küçük bir sayı giriniz...")
        print("Kalan tahmin hakkı: ",tahmin_hakki)
    else:
        print("Sayı sorgulanıyor...")
        time.sleep(1)
        tahmin_hakki -= 1
        print("Daha büyük bir sayı giriniz")
        print("Kalan hakkınız: ",tahmin_hakki)
    if tahmin_hakki == 0:
        print("Tahmin hakkınız bitmiştir",sayi)
        