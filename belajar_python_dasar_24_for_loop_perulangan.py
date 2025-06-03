# Perulangan (loop)

# for kondisi:
#   aksi

# ini dengan list
angka2_list = [0,1,2,3,4] # ini adalah list
print(angka2_list)

for i in angka2_list:
  print(f"i sekarang -> {i}")
print("akhir dari program 1\n")

# ini dengan range
angka2_range = range(5)
for i in angka2_range:
  print(f"i sekarang -> {i}")
print("akhir dari program 2\n")

angka2_range = range(1,5)
for i in angka2_range:
  print(f"i sekarang -> {i}")
print("akhir dari program 3\n")

# menggunakan string
data_str = "ricky damar saputra"
for huruf in data_str:
  print(f"huruf -> {huruf}")
print("akhir dari program 4\n")