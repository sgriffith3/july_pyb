print("Hi")

greeting = "Howdy!"

print(greeting)
print(type(greeting))

integer = 111
print(integer)
print(type(integer))

non_integer = "111"
print(non_integer)
print(type(non_integer))

result = integer - 42
print(result)

result01 = int(non_integer) - 42
print(result01)

# This fails because you can't subtract an int from a str
# result02 = non_integer - 42
# print(result02)

my_float = 99.9
print(my_float)
print(type(my_float))

result03 = integer - my_float
print(round(result03))
print(type(result03))
