import tkinter as tk
from tkinter import ttk


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



def operasi_hitung(event="none"):

    value1 = float(input1.get())
    value2 = float(input2.get())

    if not value1 or not value2:
        label_hasil.config(text="Error: Input tidak boleh kosong!")
        return



    operasi_terpilih = operasi.get()
    if operasi_terpilih == "Penjumlahan":
        hasil = value1 + value2
    elif operasi_terpilih == "Pengurangan":
        hasil = value1 - value2
    elif operasi_terpilih == "Perkalian":
        hasil = value1 * value2
    elif operasi_terpilih == "Pembagian":
        hasil = value1 / value2 if value2 != 0 else "Tidak bisa dibagi dengan nol"
    else: hasil = "Pilih Operasi terlebih dahulu"
    
    label_hasil.config(text="Hasil: " + str(hasil))

    jenis_operasi.config(text="Jenis Operasi: " + operasi_terpilih)


    


operasi = ttk.Combobox(bottom_frame, state="readonly", value=["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"])
operasi.grid(row=2, column=1)
operasi.set("Pilihan Operasi")
operasi.bind("<<ComboboxSelected>>",)

jenis_operasi = tk.Label(bottom_frame, text="Jenis Operasi: ")


button = tk.Button(bottom_frame, text='Hitung', width=25, command = operasi_hitung)
button.grid(row=3, column=1, pady=10)

label_hasil = tk.Label(bottom_frame, text = f" Hasil: ")
label_hasil.grid(row=4, column=1)
window.mainloop()
