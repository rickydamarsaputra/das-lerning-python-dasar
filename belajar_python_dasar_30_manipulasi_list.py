# Operasi

# index  0        1         2
data = ["ricky", "damar", "saputra"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0): {data_0}")
data_terakhir = data[-1]
print(f"data terakhir (index -1): {data_terakhir}")

data_damar = data[1]
print(f"data ricky: {data_damar}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data: {panjang_data}")

# manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah: {data}")
data.insert(1, "rifki")
print(f"data sesudah ditambah: {data}")

# menambah di akhir list
data.append("alam")
print(f"data ditambah lagi: {data}")

# menambahkan list dengan list
data_baru = ["naila", "salsabila", "azzahra"]
data.extend(data_baru)
print(f"data gabungan: {data}")

# merubah data
# kita ubah data ke 2 menjadi michael
data[2] = "michael"
print(f"data rubah: {data}")

# meremove data
data.remove("michael")
print(f"data remove: {data}")
# data.remove("alex") akan error karna data tidak sesuai

# meremove data paling belakang
data.pop()
print(f"data akhir: {data}")
