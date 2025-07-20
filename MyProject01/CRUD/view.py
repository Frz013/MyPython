from . import operasi

def read_console():
    isi_data = operasi.read()
    index = "No"
    penulis = "Penulis"
    judul = "Judul"
    tahun = "Tahun"

    #Header
    print("="*100 +"\n")
    print(f"{index:4} | {penulis:40} | {judul:40} | {tahun:5}")
    print("-"*100)

    #content
    for index,data in enumerate(isi_data):
        data_break = data.split(",")

        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]

        print(f"{index+1:4} | {penulis:.40} | {judul:.40} | {tahun:4}", end="")
    
    #Footer
    print("\n"+ "="*100)