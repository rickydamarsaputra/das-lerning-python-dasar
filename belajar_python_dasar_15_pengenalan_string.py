data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
  1. dengan menggunakan single quote '...'
  2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Hallo, apa kabar?"')
print("'Hallo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Ricky")

# tab
print("rick\t\t\tdamar")

# backspace
print("ricky \bdamar")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> windows

# 3. string literal ata raw

#  hati-hati
print('C:\new folder') # akan salah path

# menggunakan raw string
print(r'C:\new \t\r\b\\folder')

# multiline literal string
print("""
Nama: Ricky
Kelas: D3 Sistem Informasi
""")

# multiline literal string dan raw
print(r"""
Nama: Ricky
Kelas: D3 Sistem Informasi
Website: www.rickydamar.com/newID
""")
