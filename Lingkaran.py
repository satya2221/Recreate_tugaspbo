import  math


class Lingkaran:
    def __init__(self, djari):
        self.jari = djari

    def luas(self):
        luasnya = math.pi * math.pow(self.jari,2)
        return luasnya

    def keliling(self):
        kelilingnya = math.pi * 2 * self.jari
        return kelilingnya
