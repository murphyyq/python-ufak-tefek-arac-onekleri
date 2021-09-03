def UsAl(sayi,us):
     sonuc=1
     for i in range(us):
         sonuc=sonuc*sayi
     return sonuc

s1=int(input('Sayıyı Gir : '))
s2=int(input('Üs Gir : '))

print (s1,"'ün",s2,".","kuvveti =",UsAl(s1,s2))


