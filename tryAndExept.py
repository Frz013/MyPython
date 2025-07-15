# penggunaan try-except dalam Python

# try:
#     angka = int(input("Masukkan sebuah angka: "))
#     hasil = 10 / angka
#     print("Hasil pembagian 10 dengan", angka, "adalah", hasil)
# except ValueError:
#     print("Input bukan angka yang valid.")
# except ZeroDivisionError:
#     print("Tidak bisa membagi dengan nol.")


while(True):

    try:
        angka = int(input("masukan angka: "))
        hasil = 10/angka
        print(f"hasil: {hasil}")
        isLanjut = input("apakah ingin lanjut? (Y/n)")
        if isLanjut == "n":
            break
    except:
        print("tidak bisa membagi dengan nol")
