import sqlite3
from personel import Personel

baglanti = sqlite3.connect("personeller.db")

c = baglanti.cursor()

c.execute("""CREATE TABLE personeller (
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


def guncelleMaas(kisi, maas):
    with baglanti:
        c.execute("""UPDATE personeller SET maas = :maas
                    WHERE ad = :ad AND soyad = :soyad""",
                  {'ad': kisi.ad, 'soyad': kisi.soyad, 'maas': maas})


def silPersonel(kisi):
    with baglanti:
        c.execute("DELETE from personeller WHERE ad = :ad AND soyad = :soyad",
                  {'ad': kisi.ad, 'soyad': kisi.soyad})

atilla = Personel('Atilla', 'Beyaz', 15750)
kayra = Personel('Kayra', 'Demir', 7490)
nehir = Personel('Nehir', 'Beyaz', 9280)
mete = Personel('Mete', 'Kizil', 118400)
efe = Personel('Efe', 'Sancak', 6370)
eklePersonel(atilla)
eklePersonel(kayra)
eklePersonel(nehir)
eklePersonel(mete)
eklePersonel(efe)

beyaz = listeleSoyad('Beyaz')
print("Soyadi 'Beyaz' olan personeller ve maaslari:\n")
print(beyaz)

guncelleMaas(atilla, 17360)
silPersonel(nehir)

beyaz = listeleSoyad('Beyaz')
print("Islemlerden sonra soyadi 'Beyaz' olan personeller ve maaslari:\n")
print(beyaz)

baglanti.close()