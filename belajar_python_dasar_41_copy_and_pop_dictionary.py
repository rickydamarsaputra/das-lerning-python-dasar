# copy dictionary
teman_teman = {
  "nama": "ricky damar saputra",
  "umur": 23,
  "tinggi": 175
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}")
print(f"friends: {friends}\n")

teman_teman["nama"] = "rifki alam saputra"

print(f"teman-teman: {teman_teman}")
print(f"friends: {friends}\n")

# pop dictionary
dataNama = friends.pop("nama")
print(f"data nama: {dataNama}")
print(f"friends: {friends}\n")

# popitem dictionary
dataTerakhir = friends.popitem()
print(f"data terakhir: {dataNama}")
print(f"friends: {friends}\n")