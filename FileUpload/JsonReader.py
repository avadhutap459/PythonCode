import json

with open("D:\\Python\\Python-Sample\\FileUpload\\uploads\\user.json", "r") as file:

    user = json.load(file)

print(user)
print(user["name"])


# load() vs loads()

#load()

# JSON file → Python object

# with open("user.json", "r") as file:

#    user = json.load(file)

#loads()

# JSON string → Python object

# json_string = '{"id": 101, "name": "Avadhut"}'

# user = json.loads(json_string)

# print(user["name"])