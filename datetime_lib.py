import datetime

data_waktu = datetime.datetime.now().date()

hari = data_waktu.strftime("%A")
tanggal = data_waktu.strftime("%d")
bulan = data_waktu.strftime("%B")
tahun = data_waktu.strftime("%Y")

print(hari, tanggal, bulan, tahun)