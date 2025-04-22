import string
import time
import random
import os

os.system('clear')

text = 'HELLO, WORLD'
huruf_valid = string.ascii_uppercase + ' ,' + '!' + '?'
huruf_acak = string.ascii_uppercase + ' '
temp = ''

for char in text:
    for i in huruf_valid:
        if i not in huruf_valid:
            continue

        sisa_panjang = len(text) - len(temp) - 1
        random_chars = ''.join(random.choice(huruf_acak) for _ in range(sisa_panjang))

        output = temp + i + random_chars

        padded_output = output.ljust(len(text))

        print(padded_output)
        time.sleep(0.025)

        if i == char:
            temp += char
            break

for i in range(5):
    print(text)
    time.sleep(0.025)