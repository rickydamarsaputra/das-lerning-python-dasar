import sains.matematika
from sains import fisika
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1,4,6,8,4)
print(f"hasil tambah dari package adalah: {hasil_tambah}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah: {gaya}")

gaya = force(80,10)
print(f"gaya adalah: {gaya}")
