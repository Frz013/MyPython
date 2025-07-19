import os



if __name__ == "__main__":
    sistem_operasi = os.name

    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
    
        ### Input 
        print("SELAMAT DATANG DI PROGRAM DATABASE PERPUSTAKAAN")
        print("="*47)

        print("1. READ")
        print("2. ADD DATA")
        print("3. UPDATE DATA")
        print("4. REMOVE DATA\n")

        pilihan_user = int(input("MASUKAN PILIHAN OPSI: "))