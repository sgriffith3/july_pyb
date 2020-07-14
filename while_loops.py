# While loop

x = 0

while isinstance(x, int):
    print(x)
    x = x + 1
    if x == 3:
        continue
    print("some specific action")
    if x == 7:
        break
