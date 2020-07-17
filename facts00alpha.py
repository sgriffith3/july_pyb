#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    sites = ["http://api.open-notify.org/astros.json", "https://cat-fact.herokuapp.com/facts", "https://2.python-requests.org//en/master/"]

    # display the methods available to our new object
    #print( dir(r) )
    for site in sites:
        r = requests.get(site)
        if r.status_code == 200:
            print(f"{site} worked!")
        else:
            print(f":[ {site} failed!")
main()

