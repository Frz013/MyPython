import os
import CRUD as CRUD


if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    
    print("SELAMAT DATANG DI PROGRAM DATABASE PERPUSTAKAAN")
    print("="*47)

    CRUD.init_console()

    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
    
        ### Input 
        print("SELAMAT DATANG DI PROGRAM DATABASE PERPUSTAKAAN")
        print("="*47)

        print("1. READ DATA")
        print("2. ADD DATA")
        print("3. UPDATE DATA")
        print("4. REMOVE DATA\n")

        pilihan_user = int(input("MASUKAN PILIHAN OPSI: "))

        print("\n","="*47,"\n")

        try:
            match pilihan_user:
                case 1: print("READ DATA")
                case 2: print("ADD DATA")
                case 3: print("UPDATE DATA")
                case 4: print("REMOVE DATA")
                case _: print("INPUT TIDAK VALID, PILIH 1-4!")
        except ValueError:
            print("HARUS ANGKA!")

        print("\n","="*47,"\n")

        isCon = input("apakah ingin lanjut? (y/n)")
        if isCon == "n" or isCon == "N":
            break