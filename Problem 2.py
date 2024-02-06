fish = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory", "red cod"]

print("First letter:") #A

for thing in fish:
    print(thing[0])

print("\nFirst 3 letters:") #B

for thing in fish:
    print(thing[0:3])

print("\nLongest name:") #C

fish_len = sorted(fish, key=len)
print(fish_len[-1])

print("\nMore than 1 word:") #D

space_names = []

for name in fish:
    if " " in name:
        space_names.append(name)

for name in space_names:
    print(name)

print("\nCod in name:") #E

cod_names = []

for name in fish:
    if "cod" in name:
        cod_names.append(name)

for name in cod_names:
    print(name)



