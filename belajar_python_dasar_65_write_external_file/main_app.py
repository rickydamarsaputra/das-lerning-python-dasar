# 1. mode write, 
# dia akan membuat file baru jika tidak ada
# lalu akan menimpa/overwrite isinya

with open("data_1.txt","w", encoding="utf-8") as file:
  file.write("ricky damar saputra")

with open("data_1.txt","w", encoding="utf-8") as file:
  file.write("rifki alam saputra")

with open("data_1.txt","w", encoding="utf-8") as file:
  file.write("naila salsabila azzahra")

# 2. mode append

with open("data_2.txt","w", encoding="utf-8") as file:
  file.write("ricky damar saputra\n")

with open("data_2.txt","a", encoding="utf-8") as file:
  file.write("rifki alam saputra\n")

with open("data_2.txt","a", encoding="utf-8") as file:
  file.write("naila salsabila azzahra")

# 3. mode r+

with open("data_3.txt", "w", encoding="utf-8") as file:
  file.write("data ke 3\n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
  file.write("baris-1\n")
  file.write("baris-2\n")

with open("data_3.txt", "r+", encoding="utf-8") as file:
  data = file.read()
  print(data)

with open("data_3.txt", "r+", encoding="utf-8") as file:
  file.write("baris-3\n")