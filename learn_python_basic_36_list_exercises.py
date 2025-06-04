#  program list buku

list_buku = []
while True:
  print("Masukan data buku")
  judul = input("Judul buku\t: ")
  penulis = input("Nama penulis\t: ")

  buku_baru = [judul, penulis]
  list_buku.append(buku_baru)
  
  print("No.\t| Judul\t\t| Penulis")
  for index,buku in enumerate(list_buku):
    print(f"{(index + 1)}\t| {buku[0]}\t| {buku[1]}")

  isLanjut = input("Apakah dilanjutkan?(y/n): ")

  if isLanjut == "n": 
    break

print("PROGRAM SELESAI")