with open("D:\\Python\\Example.txt", "rb") as file:

    data = file.read()

    print(type(data))
    
print("Example ::: Read specific number of byte")
with open("D:\\Python\\Example.txt", "rb") as file:

    data = file.read(10)

    print(data)
    
