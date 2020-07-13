# Create a list of cars with at least 5 elements in it
cars = ["civic", "911", "f-type", "armada", "caravan"]

# Create a list of names with at least 5 elements in it
names = ["Steve", "Bill", "Chuck", "Larry", "Bob"]

# Print out items from the third index of each list
print(cars[3])
print(names[3])

# Print out the slice containing items from cars at indices 2-4 (inclusive)
print(cars[2:])

# Print out the slice containing items from names at indices 0-2 (non-inclusive)
print(names[0:2])

# Create a blank list named combined
combined = []

# Use the append method to add the cars into the list
combined.append(cars)

# Use the extend method to add the names into the list
combined.extend(names)

# Print out 2 cars and 2 names from combined list
print(combined)

# [['civic', '911', 'f-type', 'armada', 'caravan'], 'Steve', 'Bill', 'Chuck', 'Larry', 'Bob']
print(combined[0][0])
print(combined[0][1])

print(combined[2], combined[4])

# Concatenation
my_str = combined[2] + ' is cooler than ' + combined[4]
print(my_str)


better_str = "{} is better than {}".format(combined[4], combined[2])
print(better_str)

