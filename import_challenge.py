# Importing from your own code

# Create two files, named "core.py" and "app.py"

# Inside of your core.py file, create a function named silly_strings
# The silly_strings function should take one parameter, a list of strings

# example words
words = ["Sam", "is", "a", "duck"]

#Pig latin generator

VOWELS = ('a', 'e', 'i', 'o', 'u')

txt = ""
for word in words:
    if word.startswith(VOWELS):
        txt += f"{word}ay "
    else:
        txt += f"{word[1:]}{word[:1]}ay "


# From you app.py, get three or more user inputs for silly words
# Put them into a list
# Import you silly_strings function from your core.py script
# Pass the list into the silly_strings function and print the result
