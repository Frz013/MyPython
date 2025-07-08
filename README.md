# MyPython Project

Ini adalah kumpulan program Python yang saya buat untuk belajar dan latihan. Di dalamnya ada berbagai contoh aplikasi mulai dari kalkulator matematika, pengelolaan data, animasi terminal, hingga tampilan grafis (GUI) dengan Tkinter dan Pygame. Cocok untuk pemula yang ingin memahami dasar-dasar pemrograman Python, matematika, fisika, serta penggunaan library populer seperti Tkinter, Pygame, dan NumPy.

---

## Daftar Isi

- [Matrix Calculator](#matrix-calculator)
- [Falling Text](#falling-text)
- [Penjelasan Tiap File](#penjelasan-tiap-file)
- [Cara Menjalankan](#cara-menjalankan)
- [Kebutuhan Sistem & Library](#kebutuhan-sistem--library)

---

# Matrix Calculator

Matrix Calculator adalah program sederhana untuk melakukan operasi dasar pada matriks menggunakan NumPy. Fitur yang tersedia:

### Fitur

1. **Pilih Ukuran Matriks**
   - Bisa memilih matriks 2x2 atau 3x3.

2. **Operasi Matriks**
   - Penjumlahan
   - Pengurangan
   - Perkalian
   - Transpose
   - Determinan
   - Invers

3. **Input Data**
   - Pengguna diminta memasukkan elemen-elemen matriks A (dan B jika diperlukan) dalam satu baris, dipisah spasi.

4. **Output**
   - Program menampilkan matriks A, B (jika ada), dan hasil operasinya.

### Cara Pakai

1. Jalankan program matrix calculator.
2. Pilih ukuran matriks (2x2 atau 3x3).
3. Pilih jenis operasi (1-6).
4. Masukkan elemen-elemen matriks A (dan B jika perlu), misal: `1 2 3 4` untuk 2x2.
5. Hasil operasi akan ditampilkan di layar.

---

# Falling Text

Animasi teks di terminal, di mana kalimat **"HELLO, WORLD"** muncul satu per satu dari atas ke bawah, seperti efek jatuh. Setiap huruf ditebak secara acak sampai cocok, lalu lanjut ke huruf berikutnya.

### Penjelasan

1. **Import Library**
   - `string`, `random`, `time`, `os` untuk kebutuhan animasi dan manipulasi terminal.

2. **Bersihkan Layar**
   - Agar animasi terlihat rapi.

3. **Set Kalimat**
   - Kalimat yang akan dianimasikan: "HELLO, WORLD".

4. **Proses Animasi**
   - Setiap huruf ditebak acak sampai benar, lalu ditampilkan satu per satu.

5. **Tampilan**
   - Huruf-huruf muncul dari atas ke bawah, menciptakan efek jatuh.

---

# Penjelasan Tiap File

Berikut penjelasan fungsi setiap file Python di proyek ini:

## 1. `math_module.py`
- Berisi fungsi operasi matematika dasar: tambah, kurang, kali, bagi.
- Fungsi faktorial (rekursif).
- Fungsi pangkat dan modulus menggunakan lambda.
- Semua fungsi menerima argumen dinamis.

## 2. `dictionary.py`
- Program untuk mengelola data mahasiswa.
- Input: nama, NIM, SKS lulus, tanggal lahir.
- Data disimpan dalam dictionary dengan key acak.
- Menampilkan data mahasiswa dalam bentuk tabel setiap kali data baru ditambahkan.

## 3. `trianggle.py`
- Menampilkan berbagai pola segitiga bintang di terminal:
  - Segitiga naik, turun, piramida, dan piramida terbalik.
- Jumlah baris ditentukan oleh input user.

## 4. `datetime_lib.py`
- Menampilkan hari, tanggal, bulan, dan tahun saat ini.
- Menampilkan jam yang terus diperbarui setiap detik di terminal.

## 5. `pygame_lib.py`
- Contoh penggunaan library Pygame.
- Membuat jendela grafis 500x500 piksel.
- Kotak biru yang dapat digerakkan dengan tombol panah pada keyboard.

## 6. `tkinter_lib.py`
- GUI sederhana menggunakan Tkinter.
- Menu utama dengan tombol untuk membuka kalkulator normal, kalkulator matriks, dan kalkulator suhu.
- Kalkulator normal: operasi tambah, kurang, kali, bagi.
- Kalkulator matriks: operasi matriks 2x2 dan 3x3 (penjumlahan, pengurangan, perkalian, transpose, determinan, invers).
- Kalkulator suhu: (fitur dapat dikembangkan) untuk konversi suhu antar satuan.

## 7. `import.py`
- Program utama berbasis terminal.
- Menyediakan menu untuk kalkulasi matematika dasar, operasi matriks, dan konversi suhu.
- Menggabungkan berbagai modul lain (`math_module`, `mtx`, `fisika`).

## 8. `calculation/fisika.py`
- Berisi fungsi konversi suhu antar satuan:
  - Celcius, Reamur, Fahrenheit, Kelvin.
- Menu interaktif untuk memilih jenis konversi dan memasukkan nilai suhu.

---

## Cara Menjalankan

1. Pastikan Python 3 sudah terinstall di komputer.
2. Install library tambahan jika diperlukan:
   ```bash
   pip install numpy pygame
   ```
3. Jalankan file yang diinginkan:
   - Untuk kalkulator utama (terminal):  
     ```bash
     python import.py
     ```
   - Untuk GUI kalkulator:  
     ```bash
     python tkinter_lib.py
     ```
   - Untuk animasi terminal:  
     Jalankan script animasi yang diinginkan.
   - Untuk eksperimen lain, jalankan file terkait sesuai kebutuhan.

---

## Kebutuhan Sistem & Library

- Python 3.x
- [NumPy](https://numpy.org/) (untuk operasi matriks)
- [Pygame](https://www.pygame.org/) (untuk grafis sederhana)
- [Tkinter](https://wiki.python.org/moin/TkInter) (biasanya sudah ada di Python)
- OS: Windows (beberapa script menggunakan `os.system('cls')`)

---

**Catatan:**  
Setiap file dapat dijalankan secara terpisah untuk belajar konsep tertentu, atau digunakan bersama melalui file utama (`import.py`).  
Silakan modifikasi dan kembangkan sesuai kebutuhan belajar masing-masing.

