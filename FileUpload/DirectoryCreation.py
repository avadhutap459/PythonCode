import os

folder_path = "D:\\Python\\Python-Sample\\FileUpload\\uploads1"


if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_path = os.path.join(
    folder_path,
    "test.txt"
)

with open(file_path, "w") as file:
    file.write("Hello Python")

print("File created")