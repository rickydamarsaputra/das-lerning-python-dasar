# operator dalam bentuk methods

# merubah case dari string

# merubah semua ke upper case
salam = "assalamualaikum"
print("normal: ", salam)
salam = salam.upper()
print("upper: ", salam)

# merubah semua ke lower case
alay = "aKu KeCe AbiezzZZzzzZZ"
print("normal: ", alay)
alay = alay.lower()
print("lower: ", alay)

# pengecekan dengan isX method
# contoh pengecekan lower case
salam = "selamat pagi"
apakah_lower = salam.islower() # hasilnya akan boolean
print(salam + " is lower: " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya akan boolean
print(salam + " is upper: " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okey Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya boolean

print(judul + " is title = " + str(cek_judul))

# ngecek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start: " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Oppa")
print("end: " + str(cek_end))

# penggabungan komponen join() split()
pisah = ['ricky', 'damar', 'saputra']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabungan = ' sir '.join(pisah)
print(gabungan)

gabungan = "rickysirdamarsirsaputra"
print(gabungan.split('sir'))

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20, "🔥")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip("🔥") # menghilangkan tanda 🔥
print("'"+tengah+"'")