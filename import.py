# import math_module as  mtk
# import matrix as mtx

from calculation import mtk, mtx, fisika

print("="*15 + " Selamat datang di kalkulator operasi perhitungan dasar matematika " + "="*15 + "\n")
print("Silahkan pilih operasi yang di inginkan: ")
operasi = int(input("1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Pangkat\n6. Faktorial\n7. Modulus\n8. Operasi Matrix\n9. Konversi satuan suhu\n"))

if operasi == 1:
    print("="*7 + " Penjumlahan" + "="*7)
    nilai = list(map(int, input("masukan nilai a+b+c+... dst (hanya angka dan dipisah spasi): ").split()))
    print(f"Hasilnya adalah: {mtk.tambah(*nilai)}")

elif operasi == 2:
    print("="*7 + " Pengurangan" + "="*7)
    nilai = list(map(int, input("masukan nilai a-b-c-... dst (hanya angka dan dipisah spasi): ").split()))
    print(f"Hasilnya adalah: {mtk.kurang(*nilai)}")

elif operasi == 3:
    print("="*7 + " Perkalian" + "="*7)
    nilai = list(map(int, input("masukan nilai a*b*c*... dst (hanya angka dan dipisah spasi): ").split()))
    print(f"Hasilnya adalah: {mtk.kali(*nilai)}")

elif operasi == 4:
    print("="*7 + " Pembagian" + "="*7)
    nilai = list(map(int, input("masukan nilai a/b/c/... dst (hanya angka dan dipisah spasi): ").split()))
    print(f"Hasilnya adalah: {mtk.bagi(*nilai)}")

elif operasi == 5:
    print("="*7 + " Pangkat" + "="*7)
    nilai = list(map(int, input("masukan nilai a pangkat b (hanya angka dan dipisah spasi): ").split()))
    print(f"Hasilnya adalah: {mtk.pangkat(*nilai)}")

elif operasi == 6:
    print("="*7 + " Faktorial" + "="*7)
    nilai = list(map(int, input("masukan nilai n! (hanya angka dan dipisah spasi): ").split()))
    print(f"Hasilnya adalah: {mtk.faktorial(*nilai)}")

elif operasi == 7:
    print("="*7 + " Modulus" + "="*7)
    nilai = list(map(int, input("masukan nilai a mod b (hanya angka dan dipisah spasi): ").split()))
    print(f"Hasilnya adalah: {mtk.modulus(*nilai)}")

elif operasi == 8:
    mtx.main()

elif operasi == 9:
    fisika.main()