# coding=utf-8

import time
import os
import platform

def temizle ():
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')
        
    else:
        os.system('cls')
    
while True:
        zaman = time.localtime()
        yil = zaman [0]
        ay = zaman [1]
        gün = zaman [2]
        saat = zaman [3]
        dakika = zaman [4]
        saniye = zaman [5]
        
        time.sleep(1)
        temizle()
        
        print("\33[1;33mTarih: {}/{}/{}".format(gün,ay,yil))
        print("Saat: {}.{}.{}".format(saat,dakika,saniye))
        
        # print("""
        # tarih: {}/{}/{}
        # saat : {}:{}:{}
        # """.format(gün, ay, yil, saat, dakika, saniye))