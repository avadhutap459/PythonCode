# Polymorphism and Type of Polymorphism

# Polymorphism is a concept in programming that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). There are two main types of polymorphism:
# 1. Compile-Time Polymorphism (Static Polymorphism): This type of polymorphism is resolved during compile time. It is achieved through method overloading and operator overloading.
# 2. Run-Time Polymorphism (Dynamic Polymorphism): This type of polymorphism is resolved during runtime. It is achieved through method overriding, where a subclass provides a specific implementation of a method that is already defined in its superclass.

# compile-Time Polymorphism Example (Method Overloading):
print("Compile-Time Polymorphism Example: Method Overloading")

class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

calc = Calculator()
calc.add(2, 3)  # This will call the second add method with three parameters, resulting in an error since Python does not support method overloading in the traditional sense.
calc.add(2, 3, 4)  # Output: 9

# How do we achieve compile-time polymorphism in Python? Python does not support traditional method overloading, but we can achieve similar functionality using default arguments or variable-length arguments.
class Calculator:   
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))  # Output: 5
print(calc.add(2, 3, 4))  # Output: 9

class Employee : 
    def __init__(self, name = None, address = None):
        if name is not None:
            self.name = "Default Name"
        else :
            self.name = name
        
        if address is not None:
            self.address = "Default Address"
        else :
            self.address = address

emp = Employee()
print(emp.name)  # Output: Default Name
print(emp.address)  # Output: Default Address

emp2 = Employee("John Doe", "123 Main St")
print(emp2.name)  # Output: John Doe
print(emp2.address)  # Output: 123 Main St

# method Overloading with Variable-Length Arguments
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(2, 3))  # Output: 5
print(calc.add(2, 3, 4))  # Output: 9

# method Overloading with Default Arguments
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))  # Output: 5
print(calc.add(2, 3, 4))  # Output: 9

# method Overloading with Different Data Types
class Calculator:
    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + " " + b
        else:
            raise TypeError("Unsupported data types")

calc = Calculator()
print(calc.add(2, 3))  # Output: 5
print(calc.add("Hello", "World"))  # Output: Hello World

#method Overloading with Different Number of Parameters
class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

calc = Calculator()
print(calc.add(2, 3))  # Output: 5
print(calc.add(2, 3, 4))  # Output: 9

#method Overloading in inheritance
class Person:
    def display_info(self):
        print("This is a person.")

class Employee(Person):
    def display_info(self):
        super().display_info()  # Call the method from the superclass
        print("This is an employee.")

employee = Employee()
employee.display_info()  # Output: This is an employee.

#method overloading in multiple inheritance
class Person:
    def display_info(self):
        print("This is a person.")

class Employee:
    def display_info(self):
        print("This is an employee.")

class Manager(Person, Employee):
    def display_info(self):
        super().display_info()  # Call the method from the first superclass (Person)
        print("This is a manager.")

manager = Manager()
manager.display_info()  # Output: This is a person. 

    

# Run-Time Polymorphism Example (Method Overriding):
print("\nRun-Time Polymorphism Example: Method Overriding")

class Person:
    def display_info(self):
        print("This is a person.")
    
class Employee(Person):
    def display_info(self):
        print("This is an employee.")

person = Person()
employee = Employee()

person.display_info()  # Output: This is a person.          
employee.display_info()  # Output: This is an employee.

# Method Overriding in Inheritance
class Person:
    def display_info(self):
        print("This is a person.")

class Employee(Person):
    def display_info(self):
        print("This is an employee.")

employee = Employee()
employee.display_info()  # Output: This is an employee.

# Method Overriding in Multilevel Inheritance
class Person:
    def display_info(self):
        print("This is a person.")

class Employee(Person):
    def display_info(self):
        print("This is an employee.")

class Manager(Employee):
    def display_info(self):
        print("This is a manager.")

manager = Manager()
manager.display_info()  # Output: This is a manager.

# Method Overriding with override keyword
class Person:
    def display_info(self):
        print("This is a person.")

class Employee(Person):
    def display_info(self):
        print("This is an employee.")

employee = Employee()
employee.display_info()  # Output: This is an employee.


