file = open('text.txt', 'r')

print(file.readline(), end="")
print(file.readlines())

file.close

with open("text.txt", "r") as file:
    isi = file.read()
    print(isi)
    print(file.closed)
print(file.closed)