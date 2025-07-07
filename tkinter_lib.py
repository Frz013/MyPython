import tkinter as tk
import numpy as np
from tkinter import ttk


def main():
    BG_COLOR = "#dceeff" 
    FRAME_COLOR = "#e3f2fd"
    TEXT_COLOR = "#0d47a1"

    main_window = tk.Tk()
    main_window.title("Menu")
    main_window.geometry("450x350")
    main_window.configure(bg=BG_COLOR)

    top_frame = tk.Frame(main_window, bg=FRAME_COLOR, bd=1, relief="ridge", )
    top_frame.pack(pady=10, padx=10, fill="x")


    bottom_frame = tk.Frame(main_window, bg=FRAME_COLOR, bd=1, relief="ridge")
    bottom_frame.pack(pady=10, padx=10, fill="both", expand=True)

    judul1 = tk.Label(top_frame, text=" Menu", font=("Helvetica", 22, "bold"))
    judul1.pack(side="top", padx=15, pady= 10)


    judul2 = tk.Label(bottom_frame, text="Pilih jenis Kalkulator", bg=FRAME_COLOR)
    judul2.grid(row=0, column=0, padx=15, pady=10)

    tombol1 = tk.Button(bottom_frame, text="Normal Kalkulator", command=normal_kalkulator)
    tombol2 = tk.Button(bottom_frame, text="Matrix Kalkulator", command=matrix_kalkulator)
    tombol3 = tk.Button(bottom_frame, text="Temperature Kalkulator")
    tombol1.grid(row=1, column=0, pady=5, padx=10)
    tombol2.grid(row=1, column=1, pady=5, padx=10)
    tombol3.grid(row=1, column=2, pady=5, padx=10)



    main_window.mainloop()


def normal_kalkulator():
    BG_COLOR = "#dceeff" 
    FRAME_COLOR = "#e3f2fd"
    TEXT_COLOR = "#0d47a1"

    window = tk.Tk()
    window.title('Kalkulator Tkinter')
    window.geometry("450x350")
    window.configure(bg=BG_COLOR)


    top_frame = tk.Frame(window, bg=FRAME_COLOR, bd=1, relief="ridge")
    top_frame.pack(pady=10, padx=10, fill="x")


    bottom_frame = tk.Frame(window, bg=FRAME_COLOR, bd=1, relief="ridge")
    bottom_frame.pack(pady=10, padx=10, fill="both", expand=True)

    label1 = tk.Label(top_frame, text="Kalkulator", font=("Helvetica", 22, "bold"), fg=TEXT_COLOR, bg=FRAME_COLOR)
    label1.pack(side="top", padx=10, pady=15)

    tk.Label(bottom_frame, text='Nilai Pertama:', bg=FRAME_COLOR, font=("Arial", 10, "bold"), fg=TEXT_COLOR).grid(row=0, column=0, sticky="w", padx=15, pady=8)
    tk.Label(bottom_frame, text='Nilai Kedua:', bg=FRAME_COLOR, font=("Arial", 10, "bold"), fg=TEXT_COLOR).grid(row=1, column=0, sticky="w", padx=15, pady=8)

    input1 = tk.Entry(bottom_frame, width=25, bg="white", fg="black", relief="flat", highlightthickness=1, highlightbackground="#90caf9")
    input2 = tk.Entry(bottom_frame, width=25, bg="white", fg="black", relief="flat", highlightthickness=1, highlightbackground="#90caf9")
    input1.grid(row=0, column=1, padx=10, pady=8)
    input2.grid(row=1, column=1, padx=10, pady=8)

    def operasi_hitung(event="none"):
        try:
            value1 = float(input1.get())
            value2 = float(input2.get())
        except ValueError:
            label_hasil.config(text="Error: Input harus angka!")
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
        else:
            hasil = "Pilih Operasi terlebih dahulu"

        label_hasil.config(text="Hasil: " + str(hasil))


    operasi = ttk.Combobox(bottom_frame, state="readonly", value=["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"])
    operasi.grid(row=2, column=1, padx=10, pady=10)
    operasi.set("Pilihan Operasi")


    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="white", background="#bbdefb", foreground="black")

    button = tk.Button(bottom_frame, text='Hitung', width=30, bg="#64b5f6", fg="white", font=("Arial", 10, "bold"),
                    relief="flat", activebackground="#42a5f5", command=operasi_hitung)
    button.grid(row=3, column=0, columnspan=2, pady=15)

    label_hasil = tk.Label(bottom_frame, text="Hasil:", bg=FRAME_COLOR, font=("Arial", 12, "bold"), fg=TEXT_COLOR)
    label_hasil.grid(row=4, column=0, columnspan=2, pady=5)

    window.mainloop()

def matrix_kalkulator():
    BG_COLOR = "#dceeff" 
    FRAME_COLOR = "#e3f2fd"
    TEXT_COLOR = "#0d47a1"

    window = tk.Tk()
    window.title('Matrix Kalkulator')
    window.geometry("450x350")
    window.configure(bg=BG_COLOR)

    top_frame = tk.Frame(window, bg=FRAME_COLOR, bd=1, relief="ridge")
    top_frame.pack(pady=10, padx=10, fill="x")

    bottom_frame = tk.Frame(window, bg=FRAME_COLOR, bd=1, relief="ridge")
    bottom_frame.pack(pady=10, padx=10, fill="both", expand=True)

    label1 = tk.Label(top_frame, text="Matrix Kalkulator", font=("Helvetica", 22, "bold"), fg=TEXT_COLOR, bg=FRAME_COLOR)
    label1.pack(side="top", padx=10, pady=15)

    tk.Label(bottom_frame, text='Masukkan Elemen Matrix A:', bg=FRAME_COLOR, font=("Arial", 10, "bold"), fg=TEXT_COLOR).grid(row=0, column=0, sticky="w", padx=15, pady=8)
    tk.Label(bottom_frame, text='Masukkan Elemen Matrix B:', bg=FRAME_COLOR, font=("Arial", 10, "bold"), fg=TEXT_COLOR).grid(row=1, column=0, sticky="w", padx=15, pady=8)
    input1 = tk.Entry(bottom_frame, width=25, bg="white", fg="black", relief="flat", highlightthickness=1, highlightbackground="#90caf9")
    input2 = tk.Entry(bottom_frame, width=25, bg="white", fg="black", relief="flat", highlightthickness=1, highlightbackground="#90caf9")
    input1.grid(row=0, column=1, padx=15, pady=8)
    input2.grid(row=1, column=1, padx=15, pady=8)

    window.mainloop()

if __name__ == "__main__":
    main()