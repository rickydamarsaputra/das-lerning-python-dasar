# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "ricky"
nama_tengah = "damar"
nama_akhir = "saputra"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untung string

# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0: ", nama_lengkap[0])
print("index ke-1: ", nama_lengkap[1])
print("index terakhir: ", nama_lengkap[len(nama_lengkap) - 1])
print("index ke-(-1): ", nama_lengkap[-1])
print("index ke-(-2): ", nama_lengkap[-2])
print("index ke-[0:3]: ", nama_lengkap[0:4])
print("index ke-[3:7]: ", nama_lengkap[3:8])
print("index ke-[0,2,4,6,8,10]: ", nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil: ", min(nama_lengkap))
# item paling besar
print("paling besar: ", max(nama_lengkap))

ascii_code = ord("'")
print("ASCII code untuk sepasi adalah", str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah", chr(data))

# 4. operator dalam bentuk method
data = "ricky damar saputra"
jumlah = data.count("a")
print("jumlah a pada " + data + " = " + str(jumlah))