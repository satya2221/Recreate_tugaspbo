import Lingkaran
import math


class Kerucut(Lingkaran.Lingkaran):
    def __init__(self, djari, tinggi):
        super().__init__(djari)
        self.tinggi_kerucut = tinggi

    def luas(self):
        tinggi_selimut = math.sqrt(math.pow(self.tinggi_kerucut, 2)
                                   + math.pow(self.jari, 2))
        luasSelimut = (Lingkaran.Lingkaran.luas(self) * tinggi_selimut) / self.jari
        luasKerucut = super().luas() + luasSelimut
        return luasKerucut

    def volume(self):
        vol_kerucut = (super().luas() * self.tinggi_kerucut) / 3
        return vol_kerucut



