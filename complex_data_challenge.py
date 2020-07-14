# Create a dictionary with 2 keys, pets and movies
# Have the value of pets be a list of dictionaries with keys of "type" and "name"
# Have the value of movies be a list of dictionaries with keys of "rating" and "name"
# pets and movies should have 3 items each

things = {"pets": [{"type": "dog", "name": "mudge"}, {"type": "fish", "name": "dorothy"}, {"type": "cat", "name": "max"}], "movies": [{"rating": "PG", "name": "Shrek"}, {"rating": "G", "name": "Lion King"}, {"rating": "PG", "name": "Chronicles of Narnia"}]}
# print out 2 of pets with their type and name

print(things["pets"][0]["type"])
print(things["pets"][0]["name"])


print(things["pets"][2]["type"])
print(things["pets"][2]["name"])

# print out 1 movie with its rating and name 
print(things["movies"][1]["rating"], things["movies"][1]["name"])

