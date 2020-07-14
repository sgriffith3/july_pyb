# Hurricane Rating System
import random

storm = random.randint(1, 200)

print(storm)
# Five 157 or greater
if storm >= 157:
    print("Cat 5")
# Four 130 to 156
elif storm >= 130:
    print("Cat 4")
# Three 111 to 129
elif storm >= 111:
    print("Cat 3")
# Two 96 to 110
elif storm >= 96:
    print("Cat 2")
# One 74 to 95
elif storm >= 74:
    print("Cat 1")
# Tropical Storm 39 to 73
elif storm >= 39:
    print("Tropical Storm")
# Tropical Depression less than or equal to 38 
else:
    print("Tropical Depression")


if storm <= 157 and storm >= 74:
    print("Cat 1, 2, 3, or 4")

elif storm >= 157 or storm <= 74:
    print("Its not a Cat 1, 2, 3, or 4")
