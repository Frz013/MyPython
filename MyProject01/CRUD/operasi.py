from . import database
from .utility import random_str
import time


def create_data():
    penulis = input("Penulis: ")
    judul = input("Judul Buku: ")
    tahun = input("Tahun terbit: ")

    data = database.TEMPLATE.copy()

    data["pk"] = random_str()
    data["date_add"] = time.