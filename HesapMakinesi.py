sayi1 = int(input("\33[93mbirinci sayıyı girin: "))
sayi2 = int(input("ikinci sayıyı girin: "))
print("\33[92m1-toplama")
print("2-çıkarma")
print("3-çarpma")
print("4-bölme","\n")
islem = int(input("işlem numarasını giriniz:",))

if (islem == 1):
    print("\33[91mSonuç: ",sayi1+sayi2)
elif (islem == 2):
    print("\33[91mSonuç: ",sayi1-sayi2)
elif (islem == 3):
    print("\33[91mSonuç: ",sayi1*sayi2)
elif (islem == 4):
    print("\33[91mSonuç: ",float(sayi1/sayi2))
else:
    print("\33[94mGeçersiz işlem")

    