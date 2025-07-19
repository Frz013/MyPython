import numpy as np

# Operasi
def Penjumlahan(a,b):
    return  a + b

def Pengurangan(a,b):
    return a - b

def Perkalian(a,b):
    return a @ b

def Transpose(a):
    return a.transpose()

def Determinan(a):
    return np.linalg.det(a)

def Invers(a):
    return np.linalg.inv(a)

def printHasil(matrixA, matrixB, matrixC, pilihanOperasi):
    if matrixB is not None:
        print(f"Matrix A:\n{matrixA}")
        print(f"Matrix B:\n{matrixB}")
        print(f"Hasil Matrix A {pilihanOperasi} Matrix B adalah:\n{matrixC}")
    else:
        print(f"Matrix A:\n{matrixA}")
        print(f"Hasil {pilihanOperasi} Matrix A adalah:\n{matrixC}")

def main():
    print("="*15 + "Matrix Calculator" + "="*15)
    print(" Pilih Operasi Matrix ")
    
    # Input
    jenisMatrix = int(input("Pilih matrix : \n 1. Matrix 2x2\n 2. Matrix 3x3\n"))
    operasi = int(input("1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Transpose\n5. Determinan\n6. Invers\n"))

    if jenisMatrix == 1:
        x, y = 2, 2
    elif jenisMatrix == 2:
        x, y = 3, 3
    else:
        print("Jenis matrix tidak valid.")
        exit()

    if operasi < 1 or operasi > 6:
        print("Operasi tidak valid. Silakan pilih antara 1 hingga 6.")
    else:
        valuesA = list(map(int, input(f"Masukkan {x*y} angka untuk matriks A (dipisah spasi): ").split()))
        matrixA = np.array(valuesA).reshape(x, y)
        matrixB = None

        if operasi <= 3:
            valuesB = list(map(int, input(f"Masukkan {x*y} angka untuk matriks B (dipisah spasi): ").split()))
            matrixB = np.array(valuesB).reshape(x, y)
    
    # Operasi
    if operasi == 1:
        matrixC = Penjumlahan(matrixA, matrixB)
        pilihanOperasi = "+"
    elif operasi == 2:
        matrixC = Pengurangan(matrixA, matrixB)
        pilihanOperasi = "-"
    elif operasi == 3:
        matrixC = Perkalian(matrixA, matrixB)
        pilihanOperasi = "*"
    elif operasi == 4:
        matrixC = Transpose(matrixA)
        pilihanOperasi = "Transpose"
    elif operasi == 5:
        matrixC = Determinan(matrixA)
        pilihanOperasi = "Determinan"
    elif operasi == 6:
        matrixC = Invers(matrixA)
        pilihanOperasi = "Invers"

    # Output
    printHasil(matrixA, matrixB, matrixC, pilihanOperasi)

if __name__ == "__main__":
    main()