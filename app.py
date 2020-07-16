# import core
# core.silly_strings(list_of_words)

from core import silly_strings


sw1 = input("Silly word #1: ")
sw2 = input("Silly word #2: ")
sw3 = input("Silly word #3: ")

latinize = [sw1, sw2, sw3]

print(silly_strings(latinize))
