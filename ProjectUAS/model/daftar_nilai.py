from view.input_nilai import *

dict = {}

def tambah():

    print("Tambah Data")
    nama = inama()
    nim = inim()
    tugas = itugas()
    uts = iuts()
    uas = iuas()
    hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35
    dict[nama] = nim, tugas, uts, uas, hasil


def ubah():
    print("Ubah Data")
    nama = input("Masukan Nama            : ")
    if nama in dict.keys():
        nim = int(input("Masukan NIM         : "))
        tugas = int(input("Nilai Tugas         : "))
        uts = int(input("Nilai UTS           : "))
        uas = int(input("Nilai UAS           : "))
        hasil = tugas * 0.30 + uts * 0.35 + uas * 0.35
        dict[nama] = nim, tugas, uts, uas, hasil
    else:
        print("Nama {0} Tidak di Tentukan".format(nama))


def hapus():
    print("Hapus Data")
    nama = input("Masukan Nama      : ")
    if nama in dict.keys():
        del dict[nama]
    else:
        print("Nama {0} Tidak di Temukan".format(nama))