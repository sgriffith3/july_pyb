# Dictionaries

# key: value
# aglet: the tip on the end of your shoelace

my_cars = {"first car": "Honda Accord"}

print(my_cars)
print(type(my_cars))
print(my_cars["first car"])

# car_list = [ "first car", "Honda Accord"]
#               0               1
# print(car_list[1])

colors = {"favorite": "Blue", "least favorite": "Brown"}
print(colors["favorite"])
print(colors["least favorite"])

print(colors.keys())

print(colors.values())

# Fails
#print(colors["worst_color"])

print(colors.get("worst_color"))
print(colors.get("favorite"))


colors["worst_color"] = "puce"
print(colors)

colors["favorite"] = "green"
print(colors)

colors.update({"ok color": ["white", "grey"] , "favorite": "yellow"})
print(colors)

# Deleting a key
del colors["ok color"]
print(colors)
