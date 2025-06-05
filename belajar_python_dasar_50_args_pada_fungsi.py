'''*args'''

# memasukan data/argument
def fungsi(nama,tinggi,berat):
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ricky", 175, 66)

def fungsi(data_list):
  data = data_list.copy()
  nama = data[0]
  tinggi = data[1]
  berat = data[2]

  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["alam", 130, 45])

# *args
def fungsi(*args):
  nama = args[0]
  tinggi = args[1]
  berat = args[2]

  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("naila", 110, 35)

# studi kasus
def tambah(*data):
  # data bertype tuple, dan bisa di iterasi
  output = 0
  for angka in data:
    output += angka
  
  return output

hasil = tambah(1,2,5,6,7,8,2)
print(f"hasil: {hasil}")

hasil = tambah(321,4,66,12,56)
print(f"hasil: {hasil}")