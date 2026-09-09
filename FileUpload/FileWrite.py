file = open("D:\\Python\\Example.txt", "w")

file.write("Hello Python")

file.close()

print("---------------Example")

with open("D:\\Python\\Example.txt", "w") as file:

    file.write("Avadhut\n")
    file.write("Python\n")
    file.write("FastAPI\n")