# pass → means "currently there is nothing inside the class"
class Employee :
    pass


class Employee :
    name = "John Doe"
    address = "123 Main St"

employee = Employee()
print(employee.name)  # Output: John Doe
print(employee.address)  # Output: 123 Main St