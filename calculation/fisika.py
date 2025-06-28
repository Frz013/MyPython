# Konversi satuan suhu
def konversi_suhu(titik_tetap_atas_Tx, titik_tetap_bawahTx, titik_tetap_atas_Ty, titik_tetap_bawahTy, suhu_diketahui):




    suhu_hasil = titik_tetap_atas_Ty - (
        (titik_tetap_atas_Tx - suhu_diketahui) / 
        (titik_tetap_atas_Tx - titik_tetap_bawahTx)
    ) * (titik_tetap_atas_Ty - titik_tetap_bawahTy)
    
    return suhu_hasil

def tampilkan_menu():
    """Menampilkan menu pilihan konversi suhu"""
    print("="*20 + " TEMPERATURE CONVERTER " + "="*20)
    print("\nPILIH JENIS KONVERSI:")
    print(" 1. Celcius ke Reamur      7. Kelvin ke Celcius")
    print(" 2. Celcius ke Fahrenheit  8. Kelvin ke Reamur")
    print(" 3. Celcius ke Kelvin      9. Kelvin ke Fahrenheit")
    print(" 4. Reamur ke Celcius     10. Fahrenheit ke Celcius")
    print(" 5. Reamur ke Fahrenheit  11. Fahrenheit ke Reamur")
    print(" 6. Reamur ke Kelvin      12. Fahrenheit ke Kelvin")
    print("\n" + "="*50)


def main():

    TITIK_DIDIH_C = 100
    TITIK_BEKU_C = 0
    
    TITIK_DIDIH_R = 80
    TITIK_BEKU_R = 0
    
    TITIK_DIDIH_F = 212
    TITIK_BEKU_F = 32
    
    TITIK_DIDIH_K = 373
    TITIK_BEKU_K = 273

    # Mapping konversi
    KONVERSI = {
        1: ("Celcius ke Reamur", TITIK_DIDIH_C, TITIK_BEKU_C, TITIK_DIDIH_R, TITIK_BEKU_R),
        2: ("Celcius ke Fahrenheit", TITIK_DIDIH_C, TITIK_BEKU_C, TITIK_DIDIH_F, TITIK_BEKU_F),
        3: ("Celcius ke Kelvin", TITIK_DIDIH_C, TITIK_BEKU_C, TITIK_DIDIH_K, TITIK_BEKU_K),
        4: ("Reamur ke Celcius", TITIK_DIDIH_R, TITIK_BEKU_R, TITIK_DIDIH_C, TITIK_BEKU_C),
        5: ("Reamur ke Fahrenheit", TITIK_DIDIH_R, TITIK_BEKU_R, TITIK_DIDIH_F, TITIK_BEKU_F),
        6: ("Reamur ke Kelvin", TITIK_DIDIH_R, TITIK_BEKU_R, TITIK_DIDIH_K, TITIK_BEKU_K),
        7: ("Kelvin ke Celcius", TITIK_DIDIH_K, TITIK_BEKU_K, TITIK_DIDIH_C, TITIK_BEKU_C),
        8: ("Kelvin ke Reamur", TITIK_DIDIH_K, TITIK_BEKU_K, TITIK_DIDIH_R, TITIK_BEKU_R),
        9: ("Kelvin ke Fahrenheit", TITIK_DIDIH_K, TITIK_BEKU_K, TITIK_DIDIH_F, TITIK_BEKU_F),
        10: ("Fahrenheit ke Celcius", TITIK_DIDIH_F, TITIK_BEKU_F, TITIK_DIDIH_C, TITIK_BEKU_C),
        11: ("Fahrenheit ke Reamur", TITIK_DIDIH_F, TITIK_BEKU_F, TITIK_DIDIH_R, TITIK_BEKU_R),
        12: ("Fahrenheit ke Kelvin", TITIK_DIDIH_F, TITIK_BEKU_F, TITIK_DIDIH_K, TITIK_BEKU_K)
    }

    tampilkan_menu()
    
    try:
        pilihan = int(input("\nMasukkan pilihan (1-12): "))
        suhu = float(input("Masukkan suhu yang akan dikonversi: "))
        
        if pilihan not in KONVERSI:
            print("Pilihan tidak valid! Harap masukkan angka 1-12.")
            return
            
        jenis, tx_atas, tx_bawah, ty_atas, ty_bawah = KONVERSI[pilihan]
        hasil = konversi_suhu(tx_atas, tx_bawah, ty_atas, ty_bawah, suhu)
        
        print(f"\nHasil konversi {jenis}:")
        print(f"{suhu}° → {hasil:.2f}°")
        
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")
    except ZeroDivisionError:
        print("Error: Pembagian dengan nol terjadi. Pastikan input valid.")







if __name__ == "__main__":
    main()