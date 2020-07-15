#Advanced Challenge

# Create a list of dictionaries with at least 5 chores in it, using the following format:
# todo = [{"chore": "dishes", "time": 15}, {"chore": "laundry", "time": 20}]
todo = [{"chore": "dishes", "time": 15}, {"chore": "laundry", "time": 20}, {"chore": "vacuuming", "time": 10}, {"chore": "pay bills", "time": 20}, {"chore": "mow yard", "time": 45}]

# Use real values to help you think about your tasks this week.

# Using a for loop, enumerate the list, capturing the index and the value
for ind, chore in enumerate(todo, 1):
# https://docs.python.org/3/library/functions.html#enumerate
    order = "first"
    if ind == 2:
        order = "second"
    elif ind == 3:
        order = "third"
    elif ind == 4:
        order = "fourth"
    elif ind == 5:
        order = "fifth"

# Use if/elif/else statement(s) to determine the order of tasks based on their index
# index 0 = first
# index 1 = second
# index 2 = third
# index 3 = fourth
# index 4 = fifth

    print(f"The {order} thing I have to do is {chore['chore']}. It should only take {chore['time']} minutes.")
# Use this sentence as a guide:
# "The {order of task} thing I have to do is {chore}. It should only take {time} minutes."

# And have your script output 5 such lines:
# "The first thing I have to do is dishes. It should only take 15 minutes."
