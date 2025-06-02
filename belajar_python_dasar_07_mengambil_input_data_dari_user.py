# mengambil input dari user

# data yang dihasilkan oleh input pasti bertype string
data = input("Masukan data: ")
print("data =", data, "type =", type(data))

# jika ingin mengambil int maka perlu dicasting
angka1 = float(input("masukan float: "))
angka2 = int(input("masukan angka: "))
print("data =", angka1, "type =", type(angka1))
print("data =", angka2, "type =", type(angka2))

# bagaimana dengan nilai boolean
binner = bool(int(input("masukan nilai boolean: ")))
print("data =", binner, "type =", type(binner))