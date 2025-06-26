def tambah(*args:int):
    if not args:
        return 0
    hasil = 0
    for i in args:
        hasil += i
    return hasil

def kurang(*args:int):
    if not args:
        return 0
    hasil = args[0]
    for i in args[1:]:
        hasil -= i
    return hasil

def kali(*args:int):
    if not args:
        return 0
    hasil = 1
    for i in args:
        hasil *= i
    return hasil

def bagi(*args:float):
    if not args:
        return 0
    if 0 in args[1:]:
        raise ValueError("Tidak bisa membagi dengan nol")
    hasil = args[0]
    for i in args[1:]:
        hasil /= i
    return hasil

def faktorial(n:int):
    if n <= 0:
        return 1
    else:
        return n*faktorial(n-1)
    
pangkat = lambda n, m : n**m

modulus = lambda n, m: n%m
