import tkinter as tk



window = tk.Tk()
window.title('TK Window')
window.geometry("500x500")

top_frame = tk.Frame(window)
top_frame.pack()

bottom_frame = tk.Frame(window)
bottom_frame.pack(pady=20)

label1 = tk.Label(top_frame, text = "Kalkulator", font=("Arial", 20), fg="black")
label1.pack(side = "top", padx = 10, pady = 10)

tk.Label(bottom_frame, text='First Value').grid(row=0)
tk.Label(bottom_frame, text='Second Value').grid(row=1)
input1 = tk.Entry(bottom_frame)
input2 = tk.Entry(bottom_frame)
input1.grid(row=0, column=1, pady=5)
input2.grid(row=1, column=1, pady=5)

def hitung():
    value1 = float(input1.get())
    value2 = float(input2.get())

    hasil = value1  + value2

    label_hasil.config(text=f"Hasil: {hasil}") 

operasi = tk.Listbox(bottom_frame, )
operasi.grid(row=3, column=1)
operasi.insert(1, "Penjumlahan")
operasi.insert(2, "Pengurangan")
operasi.insert(3, "Perkalian")
operasi.insert(4, "Pembagian")

button = tk.Button(bottom_frame, text='Hitung', width=25, command = hitung)
button.grid(row=2, column=1, pady=10)

label_hasil = tk.Label(bottom_frame, text = f" Hasil: ")
label_hasil.grid(row=4, column=1)
window.mainloop()
