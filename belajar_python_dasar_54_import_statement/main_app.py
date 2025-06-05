# import
# fungsinya adalah untuk mengambil program dari file external.py

# 1. untuk menyambung program dari external
import program_print
import program_ricky

# 2. import dengan data
import variable
import password

# data ada di namespace variable
print(variable.data)
print(password.data)

# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(4,5)
print(hasil)