# self represents the current object.
class Employee :
    def __init__(self, name, address):
        self.name = name
        self.address = address
        

employee = Employee("Jane Smith", "456 Elm St")
print(employee.name)  # Output: Jane Smith  
print(employee.address)  # Output: 456 Elm St

employee2 = Employee("Alice Johnson", "789 Oak St")
print(employee2.name)  # Output: Alice Johnson
print(employee2.address)  # Output: 789 Oak St

# Default constructor: A constructor that takes no parameters and initializes the object with default values.
class Employee:
    def __init__(self):
        self.name = "Default Name"
        self.address = "Default Address"

employee3 = Employee()
print(employee3.name)  # Output: Default Name   
print(employee3.address)  # Output: Default Address

# Parameterized Constructor: A constructor that takes parameters to initialize the object with specific values.
class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

employee4 = Employee("David Evans", "111 Birch St")
print(employee4.name)  # Output: David Evans
print(employee4.address)  # Output: 111 Birch St

# Copy Constructor: A constructor that creates a new object as a copy of an existing object.
class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    # Copy constructor
    def __copy__(self):
        return Employee(self.name, self.address)

employee5 = Employee("Eve Foster", "222 Spruce St")
employee6 = employee5.__copy__()
print(employee6.name)  # Output: Eve Foster
print(employee6.address)  # Output: 222 Spruce St

# Constructor Overloading: Python does not support constructor overloading directly, but we can achieve similar functionality using default arguments or variable-length arguments.
class Employee:
    def __init__(self, name=None, address=None):
        if name is not None and address is not None:
            self.name = name
            self.address = address
        else:
            self.name = "Default Name"
            self.address = "Default Address"

employee7 = Employee()
print(employee7.name)  # Output: Default Name
print(employee7.address)  # Output: Default Address

employee8 = Employee("Frank Garcia", "333 Pine St")
print(employee8.name)  # Output: Frank Garcia
print(employee8.address)  # Output: 333 Pine St

# Destructor: A special method that is called when an object is about to be destroyed. In Python, the destructor method is defined using the __del__() method.
class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __del__(self):
        print(f"Destructor called for {self.name}")

employee9 = Employee("Grace Harris", "444 Cedar St")
del employee9  # Output: Destructor called for Grace Harris


        