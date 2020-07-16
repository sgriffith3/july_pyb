
try:
    my_num = input("pick a number\n")
    my_num = int(my_num)
    total = 85 / my_num 
    print(total)
except ZeroDivisionError as err:
    print("Ya can't divide by 0, dummy")
    print(err)

except ValueError as err:
    print("That value is not correct")
    print(err)

except KeyboardInterrupt:
    print("\nHave a nice day!")

finally:
    print("This is the finally statement")


