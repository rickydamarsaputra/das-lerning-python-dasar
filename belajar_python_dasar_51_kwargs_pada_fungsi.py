# **kwargs

def fungsi(nama,tinggi,berat):
  # fungsi biasa
  print(f"{nama}, punya tinggi {tinggi} dan berat {berat}")

fungsi("ricky", 175, 66)

def fungsi(**kwargs):
  # fungsi biasa
  print(kwargs)

fungsi("alam", 175, 66)