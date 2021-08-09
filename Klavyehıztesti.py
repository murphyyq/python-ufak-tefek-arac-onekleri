import datetime
import time

print ("\33[93mLütfen metninizi 3 saniye sonra girin")

print ("3")
time.sleep(1)
print ("2")
time.sleep(1)
print("1")
time.sleep(1)
print ("Başla!")
time.sleep(0.2)

once = datetime.datetime.now()
yazi = input("\33[96myazmaya başla:")
sonra = datetime.datetime.now()
print("\33[93mbitti")
hiz = sonra - once
saniye = int(round(hiz.total_seconds(),2))
saniyede_harf = int(round(len(yazi) / saniye , 1))
print("\33[91mSonuç: \33[1;30m{} saniyede".format(saniye),"\33[92m{} harf yazdın".format(saniyede_harf))



