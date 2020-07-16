#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print("\n****** details of interface - " + i + " ******")
    try:
        print(
            "MAC: ", end=""
        )  # This print statement will always print MAC without an end of line
        print(
            (netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]["addr"]
        )  # Prints the MAC address
        print(
            "IP: ", end=""
        )  # This print statement will always print IP without an end of line
        print(
            (netifaces.ifaddresses(i)[netifaces.AF_INET])[0]["addr"]
        )  # Prints the IP address
    except:  # This is a new line
        print("Could not collect adapter information")  # Print an error message


def get_ip(adapter):
    print("\n****** details of interface - " + adapter + " ******")
    try:
        print(
            "IP: ", end=""
        )  # This print statement will always print IP without an end of line
        print(
            (netifaces.ifaddresses(adapter)[netifaces.AF_INET])[0]["addr"]
        )  # Prints the IP address
    except:  # This is a new line
        print("Could not collect adapter information")  # Print an error message

    return netifaces.ifaddresses(adapter)[netifaces.AF_INET][0]["addr"]


def get_mac(adapter):
    try:
        print(
            "MAC: ", end=""
        )  # This print statement will always print MAC without an end of line
        print(
            (netifaces.ifaddresses(adapter)[netifaces.AF_LINK])[0]["addr"]
        )  # Prints the MAC address
    except:
        print("Could not collect adapter information")

    return netifaces.ifaddresses(adapter)[netifaces.AF_LINK][0]["addr"]


adapter_name = input(
    "Which interface would you like the IP for?\nOptions are: lo ens3 docker0\n"
)
ip = get_ip(adapter_name)
mac = get_mac(adapter_name)

print(f"The IP for {adapter_name} is {ip}")
print(f"The MAC for {adapter_name} is {mac}")
