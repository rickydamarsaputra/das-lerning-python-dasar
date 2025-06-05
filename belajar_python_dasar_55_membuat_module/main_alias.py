# module matematika dengan import

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as terserah

# import matematika as math # <- bisa dilakukan

hasil_tambah = add(1,4,6,2,7,11)
print(f"hasil tambah: {hasil_tambah}")

hasil_kali = k(1,4,6,2,7,11)
print(f"hasil kali: {hasil_kali}")

pangkat_3 = terserah(3)
print(f"hasil pangkat3: {pangkat_3(3)}")