# Create 3 functions
# A math function that takes 2 required arguments, multiplies them together, and then divides by 100
#     and returns the result

def mult_percent(x, y):
    result = x * y
    result = result / 100
    return result

# A stringy function that takes a required argument string and returns every other letter from the string

def every_other(text):
    new_text = text[::2]
    return new_text

# A main function that calls on both of these previous functions, which has 1 required argument of an integer, and has two default arguments (1 int and 1 string)
def main(int1, int2=10, stringy="abcdefg"):
    print(mult_percent(int1, int2))
    print(every_other(stringy))


# Call on the main function

# Minimum using default values
main(20)

# Using only 1 default value
main(3, stringy="Almost break time")


main(5, stringy=4)
