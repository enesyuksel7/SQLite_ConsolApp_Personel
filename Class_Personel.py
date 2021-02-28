class Personel:

    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.ad, self.soyad)

    @property
    def adsoyad(self):
        return '{} {}'.format(self.ad, self.soyad)

    def __repr__(self):
        return "Personel('{}', '{}', {})".format(self.ad, self.soyad, self.maas)
