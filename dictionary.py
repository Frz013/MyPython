import datetime
import os

mahasiswaTemp = {
    'nama' : 'nama',
    'nim' : '00000000',
    'sks_lulus' : 0,
    'lahir' : datetime.datetime(1111,1,11),

}


dataMahasiswa = {}

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
print(mahasiswa)