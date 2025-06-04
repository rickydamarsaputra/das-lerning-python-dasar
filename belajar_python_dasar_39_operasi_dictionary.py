# operator dictionary

data_dict = {
  "nama": "ricky damar saputra",
  "umur": 23,
  "tinggi": 175
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "nama"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["nama"])
print(data_dict.get("tinggi"))
print(data_dict.get("alamat", "key tidak ditemukan")) # cek key dengan custom message

# mengupdate data
data_dict["nama"] = "rifki alam saputra" 
print(data_dict)

# menambah
data_dict["alamat"] = "sirapan rt12 rw05"
print(data_dict)

data_dict.update({"nama": "ricky damar saputra"})
print(data_dict)

data_dict.update({"no": "0895700321925"}) # menambah jika tidak ada dan mengupdate jika sudah ada
print(data_dict)

# mendelete data pada dictionary
del data_dict["no"]
print(data_dict)