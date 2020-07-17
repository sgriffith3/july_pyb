import requests

r = requests.get("http://api.open-notify.org/astros.json")

print(r)
print(r.json)
print(r.json())


data = r.json()

print(data["number"])
