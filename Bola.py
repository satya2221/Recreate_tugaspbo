import Lingkaran


class Bola(Lingkaran.Lingkaran):
    def __init__(self, djari):
        super().__init__(djari)

    def luas(self):
        luas_bola = 4 * super().luas()
        return luas_bola

    def volume(self):
        vol_bola = (4 * super().luas() * self.jari) / 3
        return vol_bola
