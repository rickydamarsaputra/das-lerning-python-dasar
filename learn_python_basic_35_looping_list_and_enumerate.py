# looping dari list

# for loop
print("for loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
  print(f"angka: {angka}")

peserta = ["ricky", "damar", "saputra"]

for nama in peserta:
  print(f"nama: {nama}")

# for loop dan range
print("\nfor loop dan range")
kumpulan_angka = [10,4,5,2,66,9]

panjang = len(kumpulan_angka)

for i in range(panjang):
  print(f"angka: {kumpulan_angka[i]}")

# while loop
print("\nwhile loop")
kumpulan_angka = [10,4,5,2,66,9]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
  print(f"angka: {kumpulan_angka[i]}")
  i += 1

# list comprehension
print("\nlist comprehension")
data = ["ricky",1,2,3,4,"damar", "saputra"]

[print(f"data: {i}") for i in data]

angka = [4,3,2,5,6,1]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\nenumerate")
data_list = ["ricky",1,2,3,4,"damar", "saputra"]

for index,data in enumerate(data_list):
  print(f"index: {index}, data: {data}")