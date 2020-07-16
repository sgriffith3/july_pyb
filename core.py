
#Pig latin generator
# pig = list of words
def silly_strings(pig):
    VOWELS = ('a', 'e', 'i', 'o', 'u') 
    txt = ""
    for word in pig:
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
    return txt


if __name__ == "__main__":
    words = ["Steve", "is", "a", "truck", "driver"]
    print(silly_strings(words))
