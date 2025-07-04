# MyPython Project
Ini adalah kumpulan program python yang saya buat untuk belajar dan berlatih.


Kumpulan program Python sederhana yang bisa dipakai untuk banyak hal, mulai dari kalkulator, ngatur data, animasi di terminal, sampai bikin tampilan grafis (GUI). Cocok banget buat kamu yang lagi belajar dasar-dasar pemrograman Python, matematika, fisika, dan juga penggunaan library keren kayak Tkinter, Pygame, dan NumPy.

---

## Daftar Isi

- [Matrix Calculator](#matrix-calculator)
- [Falling Text](#falling-text)
- [Penjelasan Tiap File](#penjelasan-tiap-file)
- [Cara Menjalankan](#cara-menjalankan)
- [Kebutuhan Sistem & Library](#kebutuhan-sistem--library)

---

# Matrix Calculator

Matrix Calculator ini program sederhana yang bisa bantu kamu ngerjain operasi-operasi dasar pada matriks. Misalnya nambah, kurang, kali, transpose, nyari determinan, sampai invers. Semuanya dibantu pakai library NumPy biar gampang.

## Fitur

1. **Pilih Ukuran Matriks**:
   - Bisa pilih matriks 2x2 atau 3x3.

2. **Operasi yang Bisa Dilakukan**:
   - Penjumlahan
   - Pengurangan
   - Perkalian
   - Transpose
   - Determinan
   - Invers

3. **Input Data**:
   - Kamu bakal diminta masukin elemen-elemen matriks A (dan B kalau perlu).

4. **Output**:
   - Program bakal nampilin matriks A, B (kalau ada), dan hasil operasinya.

## Cara Pakai

1. Jalankan programnya.
2. Pilih ukuran matriks (2x2 atau 3x3).
3. Pilih jenis operasi (dari 1 sampai 6).
4. Masukkan elemen-elemen matriks A.
5. Kalau operasinya perlu dua matriks (kayak tambah, kurang, kali), masukin juga matriks B.
6. Lihat hasilnya di layar.

---

# Falling Text

## Apa Itu Falling Text?

Ini adalah animasi teks di terminal. Jadi kalimat **"HELLO, WORLD"** muncul satu-satu hurufnya dari atas ke bawah, kayak jatuh gitu. Setiap huruf ditebak acak sampai cocok, baru lanjut ke huruf berikutnya.

### Penjelasan

1. **Import Library**:
   - `string`: buat dapetin daftar huruf.
   - `random`: buat milih huruf acak.
   - `time`: buat kasih jeda biar animasinya keliatan.
   - `os`: buat ngebersihin layar terminal.

2. **Bersihin Layar**:
   - Supaya animasinya keliatan rapi.

3. **Set Kalimat yang Ditampilkan**:
   - Kalimat yang mau ditampilkan: "HELLO, WORLD".
   - Disiapin juga daftar huruf-huruf valid dan acak buat animasinya.

4. **Proses Animasinya**:
   - Setiap huruf ditebak satu-satu secara acak sampai ketemu yang benar.
   - Tiap percobaan ditampilkan satu baris di terminal.
   - Huruf yang udah cocok ditambahin ke hasil.

5. **Tampilan di Terminal**:
   - Huruf-huruf muncul satu-satu dari atas ke bawah, kelihatan kayak efek jatuh.

---

# Penjelasan Tiap File

Berikut fungsi masing-masing file Python:

## 1. `math_module.py`
- Operasi matematika: tambah, kurang, kali, bagi.
- Fungsi faktorial (rekursif).
- Fungsi pangkat dan modulus pakai lambda.

## 2. `dictionary.py`
- Input data mahasiswa: nama, NIM, SKS, tanggal lahir.
- Data disimpan dalam dictionary dengan key acak.
- Output dalam bentuk tabel.

## 3. `trianggle.py`
- Nampilin pola segitiga bintang:
  - Segitiga naik, turun, piramida, dan piramida terbalik.
- Jumlah baris ditentukan user.

## 4. `datetime_lib.py`
- Tampilkan tanggal dan waktu sekarang.
- Jam diupdate tiap detik di terminal.

## 5. `pygame_lib.py`
- Contoh pakai Pygame.
- Bikin jendela grafis 500x500 piksel.
- Kotak biru bisa digerakin pakai tombol panah.

## 6. `tkinter_lib.py`
- GUI sederhana pakai Tkinter.
- Ada tombol buat buka kalkulator.
- Kalkulator bisa tambah, kurang, kali, dan bagi.

## 7. `import.py`
- Program utama.
- Menyediakan menu untuk kalkulasi umum, matriks, dan konversi suhu.
- Menggabungkan berbagai modul lain.

## 8. `calculation/fisika.py`
- Konversi suhu antar satuan:
  - Celcius, Reamur, Fahrenheit, Kelvin.
- Menu interaktif buat pilih jenis konversi dan masukin nilai suhu.

---

# Cara Menjalankan

1. Pastikan Python sudah terinstall di komputermu.
2. Install library tambahan (kalau belum):
   ```bash
   pip install numpy pygame
