# lambda function
def fungsi_kuadrat(angka):
  return angka**2

print(f"hasil fungsi fungsi_kuadrat: {fungsi_kuadrat(3)}")

# kita coba dengan lambda
# output lambda argument: expression
kuadrat = lambda angka:angka**2
print(f"hasil lambda kuadrat: {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lambda pangkat: {pangkat(4,2)}")

# kengunaan untuk apa?
# sorting untuk list biasa
data_list = ["ricky", "damar", "saputra"]
data_list.sort()

print(f"sorted list: {data_list}")

# sorting menggunakan panjang
data_list.sort(key=len)
print(f"sorted list by len: {data_list}")

# sort pakai lambda
data_list = ["ricky", "damar", "saputra"]
data_list.sort(key=lambda nama:len(nama))

# filter
data_angka = [1,24,7,1,5,8,9,12,34,6,3,9,12]

def kurang_dari_lima(angka):
  return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_angka_baru = list(filter(lambda x:x<5, data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x:(x%2==0), data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0), data_angka))
print(data_ganjil)

# keliparan tiga
data_3 = list(filter(lambda x:(x%3==0), data_angka))
print(f"data kelipatan 3: {data_3}")

# anonymouse function
# currying <- Haskell Curry

def pangkat(angka, n):
  hasil = angka**n
  return hasil

data_hasil = pangkat(5,2)
print(f"fungsi biasa: {data_hasil}")

# dengan currying menjadi
def pangkat(n):
  return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2: {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat 3: {pangkat3(3)}")
print(f"pangkat bebas: {pangkat(4)(5)}")