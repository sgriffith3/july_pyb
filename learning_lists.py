# Milk, Bread, Eggs

my_list = ["milk", "bread", "eggs"]
print(my_list)
print(type(my_list))

# 0. milk
# 1. bread
# 2. eggs

# my_list = ["milk", "bread", "eggs"]
#              0        1        2

print("The first item in the list is",  my_list[0])
print("The second item in the list is",  my_list[1])
print("The third item in the list are",  my_list[2])


my_list.append("bacon")
print(my_list)

your_list = my_list + ["oj"]
print(your_list)

my_list.extend(["waffles", "pancakes", "syrup"])
print(my_list)

my_list[0] = "butter"
print(my_list)

my_list.insert(0, "plate")
print(my_list)

my_list.pop()
print(my_list)



big_list = ["trash bags", "toilet paper", "aluminum foil", my_list]
print(big_list)
print(big_list[0])
print(big_list[1])
print(big_list[2])
print(big_list[3])

print(big_list[3][4])

print(big_list[0][6])











