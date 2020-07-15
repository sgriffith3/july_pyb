pets = {"cats": ["max", "garfield"], "dogs": ["bingo", "fido"]}

for pet in pets:  # This loop goes through two times
    print(f"My {pet} are:")
    #print(pets[pet])
    for name in pets[pet]: # This loop goes through two times two times (4 x)
        print(name)
    print()



for num in range(254, 267):
    print(num)


cars = ["accord", "civic", "lambo"]
for car_num, car in enumerate(cars):
    #car_num = car_num + 1
    car_num += 1
    little_letters = "st"
    if car_num == 2:
        little_letters = "nd"
    elif car_num == 3:
        little_letters = "rd"
    print(f"The car I want {car_num}{little_letters} is {car}")
    #print(car[0])
    #print(car[1])

