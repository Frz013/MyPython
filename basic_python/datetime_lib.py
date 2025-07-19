from datetime import datetime
import time

data_waktu = datetime.now().date()
data_jam = datetime.now()
hari = data_waktu.strftime("%A")
tanggal = data_waktu.strftime("%d")
bulan = data_waktu.strftime("%B")
tahun = data_waktu.strftime("%Y")

print(hari, tanggal, bulan, tahun)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("\r" + current_time, end="", flush=True)
    time.sleep(1)