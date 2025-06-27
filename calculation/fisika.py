# Konversi satuan suhu
def konversi_suhu(titik_tetap_atas_Tx, titik_tetap_bawahTx, titik_tetap_atas_Ty, titik_tetap_bawahTy, suhu_diketahui):




    suhu_hasil = titik_tetap_atas_Ty - (
        (titik_tetap_atas_Tx - suhu_diketahui) / 
        (titik_tetap_atas_Tx - titik_tetap_bawahTx)
    ) * (titik_tetap_atas_Ty - titik_tetap_bawahTy)
    
    return suhu_hasil


def main():
    print("="*15 + "Temperature Converter" + "="*15)
    print(" Pilih jenis konversi ")

    jenis_konversi = int(input("1. Celcius to Reamur \n2. Celcius to Fahrenheit \n3. Celcius to Kelvin \n4. Reamur to Celcius \n5. Reamur to Fahrenheit \n6. Reamur to Kelvin \n7. Kelvin to Celcius \n8. Kelvin to Reamur \n9. Kelvin to Fahrenheit \n10. Fahrenheit to Celcius \n11. Fahrenheit to Reamur \n12. Fahrenheit to Kelvin \n"))

    suhu = int(input("Masukan suhu yang akan dikonversi (hanya angka): "))
    titik_tetap_atas_celcius = 100
    titik_tetap_bawah_celcius = 0

    titik_tetap_atas_reamur = 80
    titik_tetap_bawah_reamur = 0

    titik_tetap_atas_fahrenheit = 212
    titik_tetap_bawah_fahrenheit = 32

    titik_tetap_atas_kelvin = 373
    titik_tetap_bawah_kelvin = 273

    if jenis_konversi == 1:
        jenis_konverter = "Celcius to Reamur"
        hasil_konversi = konversi_suhu(titik_tetap_atas_celcius, titik_tetap_bawah_celcius, titik_tetap_atas_reamur, titik_tetap_bawah_reamur, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")

    elif jenis_konversi == 2:
        jenis_konverter = "Celcius to Fahrenheit"
        hasil_konversi = konversi_suhu(titik_tetap_atas_celcius, titik_tetap_bawah_celcius, titik_tetap_atas_fahrenheit, titik_tetap_bawah_fahrenheit, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")

    elif jenis_konversi == 3:
        jenis_konverter = "Celcius to Kelvin"
        hasil_konversi = konversi_suhu(titik_tetap_atas_celcius, titik_tetap_bawah_celcius, titik_tetap_atas_kelvin, titik_tetap_bawah_kelvin, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")

    elif jenis_konversi == 4:
        jenis_konverter = "Reamur to Celcius"
        hasil_konversi = konversi_suhu(titik_tetap_atas_reamur, titik_tetap_bawah_reamur, titik_tetap_atas_celcius, titik_tetap_bawah_celcius, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")
        
    elif jenis_konversi == 5:
        jenis_konverter = "Reamur to Fahrenheit"
        hasil_konversi = konversi_suhu(titik_tetap_atas_reamur, titik_tetap_bawah_reamur, titik_tetap_atas_fahrenheit, titik_tetap_bawah_fahrenheit, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")

    elif jenis_konversi == 6:
        jenis_konverter = "Reamur to Kelvin"
        hasil_konversi = konversi_suhu(titik_tetap_atas_reamur, titik_tetap_bawah_reamur, titik_tetap_atas_kelvin, titik_tetap_bawah_kelvin, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")

    elif jenis_konversi == 7:
        jenis_konverter = "Kelvin to Celcius"
        hasil_konversi = konversi_suhu(titik_tetap_atas_kelvin, titik_tetap_bawah_kelvin, titik_tetap_atas_celcius, titik_tetap_bawah_celcius, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")

    elif jenis_konversi == 8:
        jenis_konverter = "Kelvin to Reamur"
        hasil_konversi = konversi_suhu(titik_tetap_atas_kelvin, titik_tetap_bawah_kelvin, titik_tetap_atas_reamur, titik_tetap_bawah_reamur, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")

    elif jenis_konversi == 9:
        jenis_konverter = "Kelvin to Fahrenheit"
        hasil_konversi = konversi_suhu(titik_tetap_atas_kelvin, titik_tetap_bawah_kelvin, titik_tetap_atas_fahrenheit, titik_tetap_bawah_fahrenheit, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")

    elif jenis_konversi == 10:
        jenis_konverter = "Fahrenheit to Celcius"
        hasil_konversi = konversi_suhu(titik_tetap_atas_fahrenheit, titik_tetap_bawah_fahrenheit, titik_tetap_atas_celcius, titik_tetap_bawah_celcius, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")

    elif jenis_konversi == 11:
        jenis_konverter = "Fahrenheit to Reamur"
        hasil_konversi = konversi_suhu(titik_tetap_atas_fahrenheit, titik_tetap_bawah_fahrenheit, titik_tetap_atas_reamur, titik_tetap_bawah_reamur, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")

    elif jenis_konversi == 12:
        jenis_konverter = "Fahrenheit to Kelvin"
        hasil_konversi = konversi_suhu(titik_tetap_atas_fahrenheit, titik_tetap_bawah_fahrenheit, titik_tetap_atas_kelvin, titik_tetap_bawah_kelvin, suhu)
        print(f"Hasil konversi {jenis_konverter} adalah {hasil_konversi}")







if __name__ == "__main__":
    main()