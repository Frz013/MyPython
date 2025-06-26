baris = int(input("masukan baris: "))
print("\n")

for i in range(baris, 0, -1):
    print("*" * i)
print("\n")
for j in range(1, baris+1):
    print("*" * j)
print("\n")


for k in range(1, baris+1):
    print(" "*(baris-k) + "*" * (2*k-1))
print("\n")

for l in range(baris, 0, -1):
    print(" "* (baris-l) + "*" * (2*l-1))
print("\n")
