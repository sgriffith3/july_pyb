# lists and dictionaries

vehicles = { "cars": ["civic", "accord", "lambo"], "trucks": ["F150", "Ram1500", "Sierra"] }

print(vehicles)

print(vehicles["cars"])
print(vehicles["cars"][2])

print(vehicles["trucks"])
print(vehicles["trucks"][1])


pets = {"fish": [{"type": "goldfish", "name": "wendy"}, {"type": "beta", "name": "steve"}]}

print(type(pets))
print(pets["fish"])
print(type(pets["fish"]))
print(pets["fish"][0])
print(type(pets["fish"][0]))


print(pets["fish"][0]["name"])
