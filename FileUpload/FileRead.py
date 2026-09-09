file = open("D:\\Python\\Example.txt", "r")

content = file.read()

print(content)

file.close()

print("------------Example")

with open("D:\\Python\\Example.txt", "r") as file:

    content = file.read()

    print(content)

print("------------Example ::: Read Line By Line")

with open("D:\\Python\\Example.txt", "r") as file:

    for line in file:
        print(line)
        

print("------------Example ::: Read()")

with open("D:\\Python\\Example.txt", "r") as file:

    data = file.read()

print(data)

print("------------Example ::: readline()")

with open("D:\\Python\\Example.txt", "r") as file:

    line1 = file.readline()
    line2 = file.readline()

print(line1)
print(line2)

print("------------Example ::: readlines()")
with open("D:\\Python\\Example.txt", "r") as file:

    lines = file.readlines()

print(lines)