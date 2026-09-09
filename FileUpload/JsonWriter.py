import json

user = {
    "id": 101,
    "name": "Avadhut",
    "salary": 100000,
    "skills": [
        "Python",
        "FastAPI",
        "AWS"
    ]
}

with open("D:\\Python\\Python-Sample\\FileUpload\\uploads\\user.json", "w") as file:

    json.dump(user, file, indent=4)
    


# dump() vs dumps()

#dump()

# Python object → file

# json.dump(user, file)

#dumps()

# Python object → string

# json_string = json.dumps(user)

# print(json_string)