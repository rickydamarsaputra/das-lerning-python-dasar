# Teknik menduplikat list

a = ["ricky", "damar", "saputra"]
print(f"a: {a}")

b = a # pass by reference
print(f"b: {b}")

# kita akan merubah member dari list a

# akan merubah kedua list
a[1] = "michael"
b.sort()

print(f"a: {a}")
print(f"b: {b}")

# address dari kedia list a dan b
print(f"address a: {hex(id(a))}")
print(f"address b: {hex(id(b))}")

# menduplikat list dengan copy
print("membuat list c dengan a.copy()")
c = a.copy() # full duplikat / data baru

print(f"address a: {hex(id(a))}")
print(f"address b: {hex(id(b))}")
print(f"address c: {hex(id(c))}")

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print("kita ubah data 0")
c[0] = "alam"

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print("kita ubah data 1")
c[1] = "naila"

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")