from model.daftar_nilai import *


def tampilkan():
    if dict.items():
        print("Daftar Nilai")
        print("=" * 73)
        print("|No. |    Nama    |     NIM     |  Tugas  |  UTS  |  UAS  |  Akhir       |")
        print("=" * 73)
        i = 0
        for y in dict.items():
            i += 1
            print("| {no:2} | {0:10} | {1:11} | {2:5} | {3:5} | {4:7} | {5:7} |".format
                  (y[0][:50], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))
            print("=" * 73)
    else:
        print("Daftar Nilai")
        print("=" * 73)
        print("|No. |    Nama    |     NIM     |  Tugas  |  UTS  |  UAS  |  Akhir       |")
        print("=" * 73)
        print("|                           TIDAK ADA DATA                               |")
        print("=" * 73)
def hasilpencarian():
    nama = input("Masukkan Nama        : ")
    if nama in dict.keys():
        print("\n                   DAFTAR NILAI MAHASISWA                   ")
        print("==============================================================")
        print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir  |")
        print("==============================================================")
        print("| {0:12} | {1:9} | {2:5} | {3:5} | {4:5} | {5:6}  |".format(nama, dict[nama][0], dict[nama][1], dict[nama][2], dict[nama][3], dict[nama][4]))
        print("==============================================================")
    else:
        print("Datanya {0} Tidak Ada ".format(nama))