import string
import time
import random
import os

os.system('clear')

text = 'hello world'
text = text.upper()
huruf = string.ascii_uppercase + string.whitespace + ','
huruf_acak = string.ascii_uppercase
temp = ''

for char in text:
    for i in huruf:
        random_chars = ''.join(random.choice(huruf_acak) for _ in range(len(text) - len(temp) - 1))
        
        output = temp + i + random_chars
        
        print(output)
        time.sleep(0.05)
        
        if i == char:
            temp += char
            break