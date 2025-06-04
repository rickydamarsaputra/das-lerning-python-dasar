# Fungsi dengan argument (input)

# def nama_fungsi(argument):
#   badan fungsi

def hello_world(nama):
  # fungsi hellow_world menerima input dengan variable nama
  print(f"Selamat datang {nama}")


hello_world("ricky damar saputra")
hello_world("rifki alam saputra")

# program tambah
def tambah(angka_1, angka_2):
  # fungsi tambah
  hasil = angka_1 + angka_2
  print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(2,6)

def say_hi(list_anggota):
  data_anggota = list_anggota.copy()
  for anggota in data_anggota:
    print(f"Yang terhormat {anggota}")

anggota = ["ricky", "damar", "saputra"]

say_hi(anggota)