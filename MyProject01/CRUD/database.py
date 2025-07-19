from .operasi import create_data

DB_FILE = "data.txt"
TEMPLATE = {
    "pk" : "XXXXXX",
    "date_add" : "DD-MM_YYYY",
    "judul" : " "*255,
    "penulis" : " "*255,
    "tahun" : "YYYY",
}
def init_console():

    try:
        with open(DB_FILE,"r") as file:
            print("Database tersedia")

    except:
        print("Database tidak tersedia, silahkan buat data baru: ")
        create_data()
            
