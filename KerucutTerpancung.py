import Kerucut
import math


class KerucutTerpancung (Kerucut.Kerucut):
    def __init__(self,djari,tinngi,tinggiterpancung):
        super().__init__(djari,tinngi)
        self.tinggiterpancungnya = tinggiterpancung
        self.jariatas = (self.jari * self.tinggiterpancungnya) / self.tinggi_kerucut
        self.luasalasdibuang = math.pi * math.pow(self.jariatas,2)

    def volume(self):
        volumedibuang = (self.luasalasdibuang * self.tinggiterpancungnya) / 3
        vol = super().volume() - volumedibuang
        return vol

    def luas(self):
        selimutdibuang = math.sqrt(math.pow(self.tinggiterpancungnya, 2) + math.pow(self.jariatas, 2))
        luasdibuang = math.pi * selimutdibuang * self.jariatas
        luaspermukaan = super().luas() - luasdibuang + self.luasalasdibuang
        return luaspermukaan
