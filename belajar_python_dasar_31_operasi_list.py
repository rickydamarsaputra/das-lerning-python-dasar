data_angka = [1,4,6,2,3,7,3,3,3,7,1,2]
print(f"data angka: {data_angka}")

# count data
jumlah_data_3 = data_angka.count(3)
jumlah_data_1 = data_angka.count(1)

print(f"jumlah angka 3: {jumlah_data_3}")
print(f"jumlah angka 1: {jumlah_data_1}")

# ambil posisi data (index)
data = ["ricky", "damar", "saputra"]
print(f"data: {data}")

index_damar = data.index("damar")
index_saputra = data.index("saputra")

print(f"index damar: {index_damar}")
print(f"index saputra: {index_saputra}")

# mengurutkan list
print(f"data angka sebelum sort: {data_angka}")
data_angka.sort()
print(f"data angka sesudah sort: {data_angka}")

print(f"data: {data}")
data.sort()
print(f"data sort: {data}")

# balik list
data_angka.reverse()
data.reverse()
print(f"data di reverse: \n{data_angka}\n{data}")