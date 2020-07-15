import os
import json

with open("astros.json", "r") as astros:
    data = astros.read()
    data = data.rstrip('\n')
    print(data)
    print(type(data))
    j_data = json.loads(data)
    print(type(j_data))
    # Making a directory
    if not os.path.exists("space"):
        os.mkdir("space")
    with open("space/people_in_space.txt", "w") as space_peeps:
        txt = []
        for person in j_data["people"]:
            txt.append(f'{person["name"]}\n')
        space_peeps.writelines(txt)
