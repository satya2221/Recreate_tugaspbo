import Lingkaran
import Bola
import Kerucut
import KerucutTerpancung

keluar = False
while not keluar:
    try:
        print("Menghitung Bagian Dari Lingkaran".center(40, '-'))  # hitung panjang text baru tentuin angkanya
        print("Harap masukkan bilangan positif!")
        jarinya = float(input("Masukkan Jari-Jari : "))
        tinggi = float(input("Masukkan tinggi : "))
        terpotong = float(input("Masukkan tinggi kerucut yang akan dipotong : "))
        if jarinya < 0 or tinggi < 0 or terpotong < 0:
            raise ValueError("Tidak boleh kurang dari 0")
        if tinggi < terpotong:
            raise ValueError("Tinggi terpotong melebihi tinggi kerucut asli")

        # print level 1
        print("Level 1 : ")
        lingkarannya = Lingkaran.Lingkaran(jarinya)
        print("Luas lingkaran = {}".format(lingkarannya.luas()))
        print("Keliling lingkaran = {}".format(lingkarannya.keliling()))

        # print level 2, bola
        print("Level 2 : ")
        bolanya = Bola.Bola(jarinya)
        print("Volume bola = {}".format(bolanya.volume()))
        print("Luas Bola = {} \n".format(bolanya.luas()))
        # print level 2, kerucut
        kerucutnya = Kerucut.Kerucut(jarinya, tinggi)
        print('Volume kerucut = {}'.format(kerucutnya.volume()))
        print('Luas Kerucut = {} \n'.format(kerucutnya.luas()))

        # print kerucut terpancung
        print("Level 3 : ")
        kerucut_terpancung = KerucutTerpancung.KerucutTerpancung(jarinya, tinggi, terpotong)
        print('Volume terpancung {0} = {1}'.format(terpotong, kerucut_terpancung.volume()))
        print('Luas terpancung {0} = {1} \n'.format(terpotong,kerucut_terpancung.luas()))
    except(ValueError,) as ex:
        print("error : {} ".format(ex))
    finally:
        lagi = input("Hitung lagi? (y/n) : ")
        if lagi == 'n':
            print("Gamsahamida")
            keluar = True

