import sqlite3
from Class_Personel import Personel

baglanti = sqlite3.connect("DB_Personeller.db")

c = baglanti.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS personeller (
            ad TEXT,
            soyad TEXT,
            maas INT
            )""")

def eklePersonel(kisi):
    with baglanti:
        c.execute("INSERT INTO personeller VALUES (:ad, :soyad, :maas)", {'ad': kisi.ad, 'soyad': kisi.soyad, 'maas': kisi.maas})

def listeleSoyad(gsoyad):
    c.execute("SELECT * FROM personeller WHERE soyad=:soyad", {'soyad': gsoyad})
    return c.fetchall()

def listeleTumu():
    c.execute("SELECT * FROM personeller")
    data=c.fetchall()
    print(data)

def guncelleMaas(kisi, gmaas):
    with baglanti:
        c.execute("""UPDATE personeller SET maas = :maas
                    WHERE ad = :ad AND soyad = :soyad""",
                  {'ad': kisi.ad, 'soyad': kisi.soyad, 'maas': gmaas})

def silPersonel(kisi):
    with baglanti:
        c.execute("DELETE from personeller WHERE ad = :ad AND soyad = :soyad",
                  {'ad': kisi.ad, 'soyad': kisi.soyad})

while True:
    
      try:
         i = int(input("\n1.Personel Ekle\n2.Listele\n3.Soyada Gore Listele\n4.Maas Guncelle\n5.Personel Sil\n6.Cikis\n Lutfen yapmak istediginiz islemi giriniz: "))
 
         if i==1:
             ad = str(input("Adi: "))
             soyad = str(input("Soyadi: "))
             maas = int(input("Maasi: "))
             eklenecek = Personel(ad,soyad,maas)
             eklePersonel(eklenecek)
      
         elif i==2:
             print("Kayitlar listeleniyor:")
             listeleTumu()
          
         elif i==3:
             soyad = str(input("Soyad giriniz: "))
             lsoyad=listeleSoyad(soyad)
             print(lsoyad)
            
         elif i==4:
             ad = str(input("Adi: "))
             soyad = str(input("Soyadi: "))
             gmaas = int(input("Yeni Maasi: "))
             guncellenecek = Personel(ad,soyad,gmaas)
             guncelleMaas(guncellenecek, gmaas)
             
         elif i==5:
             ad = str(input("Adi: "))
             soyad = str(input("Soyadi: "))
             maas = int(input("Maasi: "))
             silinecek = Personel(ad,soyad,maas)
             silPersonel(silinecek)
             
         elif i==6:
             baglanti.close()
             print(exit) 
             exit()
             
         else:
            print("Girdiginiz deger gecerli aralikta degildir, tekrar deneyiniz")
      
      except ValueError:
         print("Girdiginiz deger tanimsizdir, tekrar deneyiniz")
         continue
