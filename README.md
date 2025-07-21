# MyPython Project

MyPython Project adalah project yang saya buat hanya untuk latihan dan belajar

---

## Struktur Folder & File

```
MyPython/
│
├── calculation/
│   └── fisika.py         # Modul konversi suhu antar satuan (C, R, F, K)
│
├── math_module.py        # Fungsi matematika dasar (tambah, kurang, kali, bagi, faktorial, dll)
├── dictionary.py         # Pengelolaan data mahasiswa dengan dictionary
├── trianggle.py          # Menampilkan pola segitiga bintang di terminal
├── datetime_lib.py       # Menampilkan tanggal dan waktu saat ini di terminal
├── pygame_lib.py         # Contoh grafis sederhana dengan Pygame
├── tkinter_lib.py        # GUI kalkulator (normal, matriks, suhu) dengan Tkinter
├── import.py             # Program utama berbasis terminal, menggabungkan berbagai modul
├── README.md             # Dokumentasi proyek
```

**Penjelasan File/Fungsi:**

- **calculation/fisika.py**  
  Fungsi konversi suhu antar satuan (Celcius, Reamur, Fahrenheit, Kelvin) dengan menu interaktif.
- **math_module.py**  
  Fungsi matematika dasar: tambah, kurang, kali, bagi, faktorial, pangkat, modulus.
- **dictionary.py**  
  Pengelolaan data mahasiswa (nama, NIM, SKS, tanggal lahir) dalam dictionary, tampil tabel.
- **trianggle.py**  
  Menampilkan pola segitiga bintang (naik, turun, piramida, piramida terbalik) di terminal.
- **datetime_lib.py**  
  Menampilkan hari, tanggal, bulan, tahun, dan jam real-time di terminal.
- **pygame_lib.py**  
  Membuat jendela grafis 500x500 px, kotak biru bisa digerakkan dengan tombol panah.
- **tkinter_lib.py**  
  GUI kalkulator: normal (aritmatika), matriks (2x2, 3x3, berbagai operasi), suhu (konversi).
- **import.py**  
  Program utama berbasis terminal, menyediakan menu kalkulasi matematika, matriks, dan suhu.
- **README.md**  
  Dokumentasi proyek.

---

## Panduan Instalasi

### Persyaratan Sistem

- **Python**: Versi 3.x
- **OS**: Windows (beberapa script menggunakan `os.system('cls')`)
- **Library eksternal**:
  - [NumPy](https://numpy.org/) (untuk operasi matriks)
  - [Pygame](https://www.pygame.org/) (untuk grafis sederhana)
  - [Tkinter](https://wiki.python.org/moin/TkInter) (biasanya sudah ada di Python)

### Instalasi Library

Jalankan perintah berikut di terminal:
```bash
pip install numpy pygame
```
(Tkinter biasanya sudah terinstall bersama Python.)

---

## Cara Menjalankan Program

### Kalkulator Utama (Terminal)
Jalankan:
```bash
python import.py
```
Ikuti menu interaktif untuk memilih operasi matematika dasar, matriks, atau konversi suhu.

### GUI Kalkulator (Tkinter)
Jalankan:
```bash
python tkinter_lib.py
```
Pilih jenis kalkulator (normal, matriks, suhu) dari menu utama GUI.

### Animasi Terminal
Jalankan script animasi yang diinginkan, misal:
```bash
python trianggle.py
```

### Eksperimen Lain
Jalankan file terkait sesuai kebutuhan, misal:
```bash
python dictionary.py
python datetime_lib.py
python pygame_lib.py
```

---



