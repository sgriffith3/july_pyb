# Conditional Checking

# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to
# == is equal to
# != is not equal to

import random

x = random.randint(1, 100)

print(x)

if x < 10:
    print("x is less than 10")
elif x == 10:
    print("x is 10")
else:
    print("x is greater than 10")



y = True

# Positive statements
if y is True:
    print("y is True")

if y:
    print("y True")

if y == True:
    print("y == True")

# Negative Statements

# if True is not False = True
if y is not False:
    print("y is not False")

# If y is False = True
if not y:
    print("y is False")

j = False

if j:
    print("j is True")
elif not j:
    print("j is False")


txt = "This is some text"
num = 32

print(isinstance(txt, str))
if isinstance(txt, str):
    print("txt is a string")

print(isinstance(num, int))
if isinstance(num, str):
    print("num is a string")
else:
    print("num is not a string")

