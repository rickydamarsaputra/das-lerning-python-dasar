import datetime

mahasiswa1 = {
  'nama': 'ricky damar',
  'nim': '31232312320',
  'sks_lulus': 130,
  'beasiswa': False,
  'lahir': datetime.datetime(2001,10,20)
}

mahasiswa2 = {
  'nama': 'rifki alam',
  'nim': '31232312320',
  'sks_lulus': 135,
  'beasiswa': True,
  'lahir': datetime.datetime(2007,10,20)
}

mahasiswa3 = {
  'nama': 'naila salsa',
  'nim': '31232312320',
  'sks_lulus': 100,
  'beasiswa': True,
  'lahir': datetime.datetime(2015,10,20)
}

data_mahasiswa = {
  'MAH001': mahasiswa1,
  'MAH002': mahasiswa2,
  'MAH003': mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
  KEY = mahasiswa
  NAMA = data_mahasiswa[KEY]['nama']
  NIM = data_mahasiswa[KEY]['nim']
  SKS = data_mahasiswa[KEY]['sks_lulus']
  BEASISWA = data_mahasiswa[KEY]['beasiswa']
  LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')

  print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")