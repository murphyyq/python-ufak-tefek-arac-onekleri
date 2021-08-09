#coding=utf-8
import os
d = os.uname()
print(d)
print("\33[1;31mBİLGİSAYAR BİLGİLERİNİ ÖĞRENME ARACI KODED BAY MURPHYY")
print("""\33[1;34m
İşletim sitemi adı:\33[1;33m {} {}
\33[1;34mBilgisayar adı    :\33[1;33m {}
\33[1;34mSürüm             :\33[1;33m {}
\33[1;34mSürüm tarihi      :\33[1;33m {}
      """.format(
          d.sysname,d.machine,
          d.nodename,
          d.release,
          d.version
          
      ))