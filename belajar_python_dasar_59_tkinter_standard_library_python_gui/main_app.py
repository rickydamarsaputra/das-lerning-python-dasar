# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Mencoba Tkinter")

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
  # fungsi ini akan dipanggil oleh tombol
  pesan = f"Hello {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
  messagebox.showinfo("showinfo", pesan)

# frame input
input_frame = ttk.Frame(window)
# penempatan Glid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan: ")
nama_depan_label.pack(padx=10,fill="x",expand=True)

# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang: ")
nama_belakang_label.pack(padx=10,fill="x",expand=True)

# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)

# 5. Tombol
tombol_sapa = ttk.Button(input_frame, text="Sapa!", command=tombol_click)
tombol_sapa.pack(fill="x",expand=True,padx=10,pady=10)

window.mainloop()