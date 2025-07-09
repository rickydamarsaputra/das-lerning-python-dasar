from . import Operasi

def delete_console():
  read_console()
  while(True):
    print("Silahkan pilih nomor buku yang akan di delete")
    no_buku = int(input("Nomor Buku: "))
    data_buku = Operasi.read(index=no_buku)

    if data_buku:
      data_break = data_buku.split(",")
      pk = data_break[0]
      date_add = data_break[1]
      penulis = data_break[2]
      judul = data_break[3]
      tahun = data_break[4][:-1]

      print("\n"+"="*100)
      print("data yang ingin anda hapus")
      print(f"1. Judul\t: {judul:.40}")
      print(f"2. Penulis\t: {penulis:.40}")
      print(f"3. Tahun\t: {tahun:4}")

      is_done = input("Apakah anda yakin akan dihapus(y/n)? ")
      if is_done == "y" or is_done == "Y":
        Operasi.delete(no_buku)
        break
    else:
      print("Nomor tidak valid, silahkan masukan nomor lain")

  print("Data berhasil dihapus")

def update_console():
  read_console()
  while(True):
    print("Silahkan pilih nomor buku yang akan di update")
    no_buku = int(input("Nomor Buku: "))
    data_buku = Operasi.read(index=no_buku)

    if data_buku:
      break
    else:
      print("Nomor tidak valid, silahkan masukan nomor lain")

  data_break = data_buku.split(",")
  pk = data_break[0]
  date_add = data_break[1]
  penulis = data_break[2]
  judul = data_break[3]
  tahun = data_break[4][:-1]

  while(True):
    print("\n"+"="*100)
    print("Silahkan pilih data apa yang mau diubah")
    print(f"1. Judul\t: {judul:.40}")
    print(f"2. Penulis\t: {penulis:.40}")
    print(f"3. Tahun\t: {tahun:4}")

    user_option = input("Pilih data [1,2,3]: ") 
    print("\n"+"="*100)
    match user_option:
      case "1": judul = input("judul\t: ")
      case "2": penulis = input("penulis\t: ")
      case "3": 
        while(True):
          try:
            tahun = int(input("Tahun\t: ")) 
            if len(str(tahun)) == 4:
              break
            else:
              print("tahun harus angka, silahkan masukan tahun lagi")
            break
          except:
            print("tahun harus angka, silahkan masukan tahun lagi")
      case _: print("index yang dipilih tidak cocok")

    is_done = input("Apakah Selesai (y/n)? ")

    if is_done == "y" or is_done == "Y":
      break
  
  Operasi.update(no_buku,pk,date_add,tahun,judul,penulis)

def create_console():
  print("\n\n"+"="*100)
  print("Silahkan tambah data buku\n")
  
  penulis = input("Penulis\t: ")
  judul = input("Judul\t: ")
  while(True):
    try:
      tahun = int(input("Tahun\t: ")) 
      if len(str(tahun)) == 4:
        break
      else:
        print("tahun harus angka, silahkan masukan tahun lagi")
      break
    except:
      print("tahun harus angka, silahkan masukan tahun lagi")
  
  Operasi.create(tahun, judul, penulis)
  print("\nBerikut adalah data baru anda")
  Operasi.read()

def read_console():
  data_file = Operasi.read()
  
  index = "No"
  judul = "Judul"
  penulis = "Penulis"
  tahun = "Tahun"

  # Header
  print("\n"+"="*100)
  print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
  print("-"*100)
  
  # Data
  for index,data in enumerate(data_file):
    data_break = data.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4]

    print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")

  # Footer
  print("="*100+"\n")