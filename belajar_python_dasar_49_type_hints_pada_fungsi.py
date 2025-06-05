# type hints untuk fungsi
import string

# bentuk standar fungsi yang sudah kita pelajari

# studi kasus
# def fungsi(parameter):
#   hasil = parameter**2
#   print(hasil)

# fungsi(1)
# fungsi("ricky")
# fungsi(True)

# penggunaan type hints
def sepuluh_pangkat(argument:int) -> int:
  output = 10**argument
  return output

HASIL = sepuluh_pangkat(2)
print(HASIL)

def display(argument:string):
  print(argument)

display("ricky damar saputra")
