# Latihan 

# kalkulator sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("masukan angka 1: "))
operator = input("operator (+,-,x,/): ")
angka_2 = float(input("masukan angka 2: "))

# percabanganya
if operator == "+":
  hasil = angka_1 + angka_2
  print(f"hasilnya adalah {hasil}")
elif operator == "-":
  hasil = angka_1 - angka_2
  print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
  hasil = angka_1 * angka_2
  print(f"hasilnya adalah {hasil}")
elif operator == "/":
  hasil = angka_1 / angka_2
  print(f"hasilnya adalah {hasil}")
else:
  print("hasilnya adalah 'Hello, World!'")