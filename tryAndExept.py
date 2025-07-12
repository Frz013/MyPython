# penggunaan try-except dalam Python

try:
    angka = int(input("Masukkan sebuah angka: "))
    hasil = 10 / angka
    print("Hasil pembagian 10 dengan", angka, "adalah", hasil)
except ValueError:
    print("Input bukan angka yang valid.")
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol.")