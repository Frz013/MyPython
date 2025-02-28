import numpy as np
print("="*15 + "Matrix Calculator" + "="*15)
print(" Pilih Operasi Matrix ")
print("1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n")
valuesA = list(map(int, input("Masukkan 4 angka untuk matriks A (dipisah spasi): ").split()))
valuesB = list(map(int, input("Masukkan 4 angka untuk matriks B (dipisah spasi): ").split()))
 
# convert
matrixA = np.array(valuesA).reshape(2, 2)
matrixB = np.array(valuesB).reshape(2, 2)
 
# Operasi
def penjumlahan(a,b):
  return  a + b
 
# Output
matrixC = penjumlahan(matrixA,matrixB)
print("Matriks A:\n", matrixA)
print("Matriks B:\n", matrixB)
print("Hasil A + B:\n", matrixC)