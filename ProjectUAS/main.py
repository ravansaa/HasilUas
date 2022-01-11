from view.view_nilai import *

while True:
    print('=====================================')
    print('Input Data Nilai Mahasiswa'.center(40))
    print('=====================================')
    print('|    1. Tambah Data                 |')
    print('|    2. Ubah Data Mahasiswa         |')
    print('|    3. Cari Data Mahasiswa         |')
    print('|    4. Tampilkan Data Mahasiswa    |')
    print('|    5. Hapus Data Mahasiswa        |')
    print('|    6. Keluar Program              |')
    print('=====================================')
    choose = input('Pilih Menu  : ')
    if choose == '1':
        tambah()
    elif choose == '2':
        ubah()
    elif choose == '3':
        hasilpencarian()
    elif choose == '4':
        tampilkan()
    elif choose == '5':
        hapus()
    elif choose == '6':
        break
    else:
        print("Menu tidak tersedia, Silahkan pilih menu yang ada")