# **kwargs

def fungsi(nama,tinggi,berat):
  # fungsi biasa
  print(f"{nama}, punya tinggi {tinggi} dan berat {berat}")

fungsi("ricky", 175, 66)

def fungsi(**kwargs):
  # **kwargs menghasilkan dictionary
  nama = kwargs["nama"]
  tinggi = kwargs["tinggi"]
  berat = kwargs["berat"]

  print(f"{nama}, punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="alam", tinggi=175, berat=66)

# studi kasus
def math(*args, **kwargs):
  output = 0

  if kwargs["option"] == "tambah":
    for angka in args:
      output += angka
  elif kwargs["option"] == "kali":
    output = 1
    for angka in args:
      output *= angka
  else:
    print("tidak ada operasi")

  return output

hasil_jumlah = math(1,5,6,7,2,option="tambah")
hasil_kali = math(1,5,6,7,2,option="kali")

print(f"hasil jumlah: {hasil_jumlah}")
print(f"hasil kali: {hasil_kali}")