data_0 = [1,2]
data_1 = [3,4]


data_list_biasa = [1,2,3,4,5]
print(f"list biasa: {data_list_biasa}")

list_2D = [data_0, data_1, data_list_biasa, 1,7,8]
print(f"list 2D: {list_2D}")

# contoh penggunaan
peserta_0 = ["ricky", 23, "laki-laki"]
peserta_1 = ["damar", 24, "laki-laki"]
peserta_2 = ["naila", 6, "perempuan"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta: {list_peserta}")

for peserta in list_peserta:
  print(f"nama\t: {peserta[0]}")
  print(f"umur\t: {peserta[1]}")
  print(f"gender\t: {peserta[2]}\n")

# dengan reference
list_copy = list_peserta.copy();
print(f"peserta copy: {list_copy}")
peserta_0[0] = "michael"
print(f"peserta: {list_peserta}")
print(f"peserta copy: {list_copy}")
