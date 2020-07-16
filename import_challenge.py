# Importing from your own code

# Create two files, named "core.py" and "app.py"

# Inside of your core.py file, create a function named silly_strings
# The silly_strings function should take one parameter, a list of strings

# example words
words = ["Steve", "is", "a", "truck", "driver"]

#Pig latin generator

VOWELS = ('a', 'e', 'i', 'o', 'u')

txt = ""
for word in words:
    if word.startswith(VOWELS):
        txt += f"{word}"
        if word.endswith(VOWELS):
            txt += "yay "
        else:
            txt += "ay "
    else:
        cons = ""
        for letter in word:
            if letter in VOWELS:
                break
            else:
                cons += letter
        txt += f"{word[len(cons):]}{cons}ay "
print(txt)
# From you app.py, get three or more user inputs for silly words
# Put them into a list
# Import you silly_strings function from your core.py script
# Pass the list into the silly_strings function and print the result
