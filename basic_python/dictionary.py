#LEARNING DICTIONARY

import datetime
import os
import string
import random

mahasiswaTemp = {
    'nama' : 'nama',
    'nim' : '00000000',
    'sks_lulus' : 0,
    'lahir' : datetime.datetime(1111,1,11),

}


dataMahasiswa = {}

while True:
    os.system('clear')

    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswaTemp.keys())
    mahasiswa['nama'] = input("Masukkan nama mahasiswa : ")
    mahasiswa['nim'] = input("Masukkan NIM mahasiswa :")
    mahasiswa['sks_lulus'] = int(input("Masukkan jumlah SKS yang telah lulus :"))
    tgl_lahir = list(map(int, input("Masukkan tanggal,bulan,tahun lahir mahasiswa (YYYY/MM/DD)(dipisah spasi): ").split()))
    mahasiswa ['lahir'] = datetime.datetime(tgl_lahir[0],tgl_lahir[1],tgl_lahir[2])

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range (6)))
    dataMahasiswa.update({KEY : mahasiswa})

    print(f"\n{'KEY':<6} {'NAMA':<17} {'NIM':<8} {'SKS LULUS':^10} {'LAHIR':^10}")
    print("-"*60)

    for mahasiswa in dataMahasiswa:
        KEY = mahasiswa
        NAMA = dataMahasiswa[KEY] ['nama']
        NIM = dataMahasiswa[KEY] ['nim']
        SKS = dataMahasiswa[KEY] ['sks_lulus']
        LAHIR = dataMahasiswa[KEY] ['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")

    print("\n")
    isDone = input("apakah mau ditambahkan lagi? (y/n)")
    if isDone == "n":
        break

print("akhir dari program")