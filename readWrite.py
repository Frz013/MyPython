file = open('text.txt', 'r')

print(file.readline(), end="")
print(file.readlines())

file.close

with open("text.txt", "r") as file:
    isi = file.read()
    print(isi)
    print(file.closed)
print(file.closed)

with open("data.txt", "w", encoding="utf-8") as file2:
    file2.write("Hello World1\n")
    file2.write("Hello World2\n")

with open("data.txt", "r+", encoding="utf-8") as file2:
    file2.write("Hello World3\n")
    file2.write("Hello World4\n")

with open("data.txt", "r+", encoding="utf-8") as file2:
    data = file2.read()
    print(data)