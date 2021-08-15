import os
import time
import sys
from colorama import Fore,Style,Back

print(Fore.GREEN+"Şuan Bulunduğun dizin:"+Style.RESET_ALL+Fore.RED)
os.system("pwd")
print(Style.RESET_ALL)
while True:
    
    değişken1 = input(Fore.YELLOW+"dosya adı: "+Style.RESET_ALL)
    if (değişken1 == ""):
        print(Back.RED +"dosya adı boş olamaz"+Style.RESET_ALL)
    
    değişken2 = input(Fore.YELLOW+"yeni dosya adı: "+ Style.RESET_ALL)
    if (değişken1 == ""):
        print(Back.RED +"yeni ad boş geçilemez"+Style.RESET_ALL)
    
                
        print(Fore.LIGHTBLACK_EX+"çıkış yapılıyor"+Style.RESET_ALL)
        exit()
        
    os.rename(değişken1,değişken2)
   
    
    print(Fore.LIGHTRED_EX + "Dosya ismi değiştirildi yeni dosya adı:"+Style.RESET_ALL,Back.LIGHTMAGENTA_EX + değişken2 + Style.RESET_ALL)
    break