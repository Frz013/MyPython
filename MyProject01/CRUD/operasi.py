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
    data["penulis"] = penulis
    data["judul"] = judul
    data["tahun"] = tahun

    print(data["date_add"])
    input("pause")
