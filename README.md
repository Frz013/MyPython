# Matrix Calculator

Matrix Calculator adalah program sederhana yang memungkinkan pengguna untuk melakukan berbagai operasi pada matriks, termasuk penjumlahan, pengurangan, perkalian, transpose, determinan, dan invers. Program ini menggunakan library NumPy untuk memudahkan manipulasi matriks.

## Fitur

1. **Pemilihan Jenis Matriks**:
   - Pengguna dapat memilih antara matriks 2x2 atau 3x3.

2. **Operasi Matriks**:
   - Pengguna dapat memilih salah satu dari enam operasi berikut:
     - Penjumlahan
     - Pengurangan
     - Perkalian
     - Transpose
     - Determinan
     - Invers

3. **Input Matriks**:
   - Pengguna diminta untuk memasukkan elemen-elemen matriks A dan, jika diperlukan, matriks B.

4. **Output Hasil**:
   - Program akan menampilkan matriks A, matriks B (jika ada), dan hasil dari operasi yang dipilih.

## Cara Menggunakan

1. Jalankan program.
2. Pilih jenis matriks yang ingin digunakan (2x2 atau 3x3).
3. Pilih operasi yang ingin dilakukan (1-6).
4. Masukkan elemen-elemen matriks A sesuai dengan ukuran yang dipilih.
5. Jika operasi yang dipilih adalah penjumlahan, pengurangan, atau perkalian, masukkan elemen-elemen matriks B.
6. Program akan menampilkan hasil dari operasi yang dipilih.

# Falling Text

## Penjelasan Kode Animasi Teks: "HELLO, WORLD"

Kode ini membuat animasi teks di terminal, di mana huruf-huruf dari kalimat **"HELLO, WORLD"** muncul satu per satu dari atas ke bawah, seperti sedang jatuh. Setiap huruf dicoba satu per satu secara acak sampai cocok, lalu lanjut ke huruf berikutnya.

## Apa yang Dilakukan Kodenya?

### 1. Import Library
Program menggunakan beberapa pustaka Python:
- `string`: untuk mendapatkan daftar huruf alfabet.
- `random`: untuk memilih huruf secara acak.
- `time`: untuk memberi jeda (delay) agar terlihat seperti animasi.
- `os`: untuk membersihkan layar terminal sebelum memulai.

### 2. Bersihkan Layar Terminal
Sebelum animasi dimulai, layar terminal dibersihkan agar tampilannya bersih.

### 3. Tentukan Huruf yang Akan Ditampilkan
Program menyiapkan:
- `text`: kalimat yang akan dianimasikan, yaitu `"HELLO, WORLD"`.
- `huruf_valid`: semua karakter yang mungkin digunakan (huruf besar, spasi, dan koma).
- `huruf_acak`: karakter yang dipakai untuk efek acakan.
- `temp`: untuk menyimpan huruf yang sudah berhasil ditemukan.

### 4. Proses Animasi
Untuk setiap huruf dalam `text`, program:
- Mencoba berbagai karakter hingga menemukan huruf yang sesuai.
- Menampilkan hasil percobaan di terminal, satu baris untuk setiap percobaan.
- Menambahkan huruf tersebut ke `temp` setelah cocok, lalu lanjut ke huruf berikutnya.

### 5. Tampilan di Terminal
Hasil setiap percobaan ditampilkan di baris baru. Dengan begitu, kamu bisa melihat huruf-huruf terbentuk perlahan dari atas ke bawah, menciptakan efek animasi seperti "jatuh".

### ### ####
