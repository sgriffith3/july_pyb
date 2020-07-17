#!/usr/bin/env python3
import urllib.request
import re

print("Where should we search?")
url = input()
print("Great! So we'll try to open this url " + str(url) + "to search for the phrase:")

while True:
    searchFor = input("What string would you like to search for? Or, type 'quit' to exit.\n")
    if searchFor.lower() == 'quit' or searchFor.lower() == "q":
        break
    searchMe = urllib.request.urlopen(url).read().decode("utf-8")
    
    if re.search(searchFor, searchMe):
        print("Found a match!")
        num_results = re.findall(searchFor, searchMe)
        print(len(num_results))
    else:
        print("No match!")
    
