import time


boy = int(input("\33[1;34mBoyunuzu girin santimetre cinsinden (cm): "))
kilo = float(input("\33[1;33mKilonuzu girin: "))
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(0.2)
formul = kilo / ((boy/100)**2)
print("Vücut kitle endeksiniz {}".format(round(formul,2)))
print("durumunuz: ")
if (formul <= 18.5):
    print("\33[1;31mZayıf")
    print("{} Kilogram almanız gerekiyor".format(round(18.5*((boy/100)**2)- kilo , 2)))
elif (formul <= 24.9):
    print("\33[1;36mNormal")
elif (formul<= 29.9):
    print("\33[1;31mFazla Kilolu")
    print("{} kilogram zayıflamanız gerekiyor zayıf olmak istiyorsanız".format(round(kilo - 24.9*((boy/100)**2),2)))
elif (formul <= 39.9):
    print("\33[1;31mObez")
    print("{} kilogram zayıflamanız gerekiyor zayıf olmak istiyorsanız".format(round(kilo - 24.9*((boy/100)**2),2)))
else:
    print("\33[0;41mAşırı Obez")
    print("\33[0;41m {} kilogram vermeniz gerekiyor zayıflamak istiyorsanız".format(round(kilo - 24.9 *((boy/100)**2),2)))
