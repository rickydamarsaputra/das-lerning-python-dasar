# Global dan local scope

nama_global = "ricky" # <- variable global

# akses variable global dalam fungsi
def fungsi1():
  print(f"fungsi1 menampilkan {nama_global}")

fungsi1()

# akses variable global dalam fungsi
for i in range(0,5):
  print(f"loop {i} - {nama_global}")

# percabangan
if True:
  print(f"if menampilkan {nama_global}")

# variable local scope
def fungsi2():
  nama_local = "alam" # <- variable local scope

fungsi2()
# print(nama_local) tidak bisa dilakukan

# contoh 1: penggunaan
def say_ricky():
  print(f"hello {nama}")

nama = "ricky"
say_ricky()

# contoh 2: merubah variable global
angka = 0
def ubah_angka(nilai_baru):
  global angka # fungsi ini mendapat akses merubah angka
  angka = nilai_baru

print(f"sebelum: {angka}")
ubah_angka(10)
print(f"sesudah: {angka}")

# contoh 3: 
angka = 0

for i in range(0,5):
  angka += 1
  angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
  angka = 10
  angka_dummy = 10

print(angka)
print(angka_dummy)