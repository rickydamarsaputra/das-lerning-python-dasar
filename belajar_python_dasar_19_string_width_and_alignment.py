# width and multiline

# data
data_nama = "ricky damar saputra"
data_umur = 23
data_tinggi = 175
data_nomor_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"=" + "Data String" + 5*"=")
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string)

# mengatur lebar
data_nama = "ricky"
data_string = f"""
nama    = {data_nama}
nama    = {data_nama:>7}
umur    = {data_umur:>7}
tinggi  = {data_tinggi:>7}
sepatu  = {data_nomor_sepatu:>7}
"""
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string)