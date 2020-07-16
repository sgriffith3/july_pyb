# Handling Errors Challenge


# Create a function that takes a required argument of a list, and an optional parameter of an integer 
def using_try(my_list, num=5):
    # Iterate through each item of the list
    for item in my_list:
        print(item)
        # Use a try/except block to "try" to divide each item by your optional integer parameter
        try:
            result = item / num
            print(result)
        except TypeError as err:
            print(err)
            print(f"Your item {item} is not divisible by {num}")
        except ZeroDivisionError as err:
            print(err)
# If there is a TypeError, handle it by printing out the value of the error (err) and also printing "Your item ____ is not divisible by ____ " (fill in with item of list, and optional integer)
# Execute the function

# Use the list below (or one like it) to accomplish this task
mixed = ["cats", 24, "lizards", 7, "fish", 300]

using_try(mixed)
using_try(mixed, 0)
