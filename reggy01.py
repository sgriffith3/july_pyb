#!/usr/bin/env python3
import urllib.request
import re


while True:

    print("Where should we search? Or, type 'quit' to exit.")
    url = input()
    if url.lower() == 'quit' or url.lower().startswith('q'):
        break
    print("Great! So we'll try to open this url " + str(url) + "to search for the phrase:")
    searchFor = input()
    searchMe = urllib.request.urlopen(url).read().decode("utf-8")
    
    if re.search(searchFor, searchMe):
        print("Found a match!")
    else:
        print("No match!")
    
