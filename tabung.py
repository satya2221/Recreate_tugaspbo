import Lingkaran


class Tabung(Lingkaran.Lingkaran):
    def __init__(self, djari, tinggi):
        super().__init__(djari)
        self.tinggi_tabung = tinggi

    def luas(self):
        luas = (2 * super().luas()) + (super().keliling() * self.tinggi_tabung)
        return luas

    def volume(self):
        vol = super().luas() * self.tinggi_tabung
        return vol
