import numpy as np
print("="*15 + "Matrix Calculator" + "="*15)
print(" Pilih Operasi Matrix ")

# Input
operasi = int(input("1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n"))

valuesA = list(map(int, input("Masukkan 4 angka untuk matriks A (dipisah spasi): ").split()))
valuesB = list(map(int, input("Masukkan 4 angka untuk matriks B (dipisah spasi): ").split()))
 
# Convert 
matrixA = np.array(valuesA).reshape(2, 2)
matrixB = np.array(valuesB).reshape(2, 2)
 
# Operasi
def penjumlahan(a,b):
    return  a + b

def Pengurangan(a,b):
    return a - b

def Perkalian(a,b):
    return a @ b

# Case
if operasi == 1:
    matrixC = penjumlahan(matrixA,matrixB)
    pilihanOperasi = "+"
elif operasi == 2:
    matrixC = Pengurangan(matrixA,matrixB)
    pilihanOperasi = "-"
elif operasi == 3:
    matrixC = Perkalian(matrixA,matrixB)
    pilihanOperasi = "*"
# Output
print("Matriks A:\n", matrixA)
print("Matriks B:\n", matrixB)
print(f"Hasil A {pilihanOperasi} B adalah:\n {matrixC}")