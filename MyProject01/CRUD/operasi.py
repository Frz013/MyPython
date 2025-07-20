from . import database
from .utility import random_str
import time


def create_data():
    penulis = input("Penulis: ")
    judul = input("Judul Buku: ")
    tahun = input("Tahun terbit: ")

    data = database.TEMPLATE.copy()

    data["pk"] = random_str(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H:%M:%S%z", time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun

    data_str = f" {data['pk']} | {data['date_add']} | {data['penulis']} | {data['judul']} | {data['tahun']}\n"

    try:
        with open(database.DB_FILE, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("eror")

def read():

    try:
        with open(database.DB_FILE, "r") as file:
            isi = file.readlines()
            return isi
    except:
        print("terjadi kesalahan")
        return False