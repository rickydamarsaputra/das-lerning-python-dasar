import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list_a: {list_a}")
# print(list_a**2) -> error
print(f"vector_a pangkat 2: {vector_a**2}")
print(f"vector_a kali 2: {vector_a*2}")
print(f"vector_a: {vector_a}")

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix b: \n{matrix_b}")
print(f"matrix b^2: \n{matrix_b**2}")

zeros_c = np.zeros((2,2))
print(f"zeros c: \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"ones c: \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah: \n{jumlah}")