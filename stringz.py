# Strings and String Formatting

text = "Once upon a time ..."


print(text)

# Print out the sentence: 'Our text of the day is "Once upon a time ..."'

print('Our text of the day is "', text, '".', sep='')

tod = "Our text of the day is"
month = "July"
day = 14

# cumbersome and ugly
concat_combo = tod + ' "' + text + '" on ' + month + " " + str(day)
print(concat_combo)

# better way
format_combo = '{} "{}" on {} {}.'.format(tod, text, month, day)
#               0   1       2  3           0    1      2     3
print(format_combo)


# f-string
f_string_combo = f'{tod} "{text}" on {month} {day}.'
print(f_string_combo)


text = text.upper()
print(text)

text = text.lower()
print(text)

words = text.split()
print(words)

print(" $ ".join(words))
