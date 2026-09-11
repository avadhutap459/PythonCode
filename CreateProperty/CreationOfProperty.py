# Public Property Example
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public property
        self.salary = salary  # Public property

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
    
employee = Employee("John Doe", 50000)
# Accessing public properties directly
print(employee.name)  # Output: John Doe
print(employee.salary)  # Output: 50000
employee.display()  # Output: Name: John Doe, Salary: 50000

# Protected Property Example
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public property
        self._salary = salary  # Protected property

    def display(self):
        print(f"Name: {self.name}, Salary: {self._salary}")
        
employee = Employee("Jane Smith", 60000)
# Accessing protected property directly (not recommended)
print(employee.name)  # Output: Jane Smith
print(employee._salary)  # Output: 60000 (not recommended to access directly)

# Private Property Example
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public property
        self.__salary = salary  # Private property

    def display(self):
        print(f"Name: {self.name}, Salary: {self.__salary}")

employee = Employee("Alice Johnson", 70000)
# Accessing private property directly (will raise AttributeError)
# print(employee.__salary)  # Uncommenting this line will raise an AttributeError
employee.display()  # Output: Name: Alice Johnson, Salary: 70000    

#Declare public property using the @property decorator
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public property
        self._salary = salary  # Protected property

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

employee = Employee("Bob Brown", 80000)
# Accessing public property using the @property decorator   
print(employee.salary)  # Output: 80000
employee.salary = 90000  # Setting a new salary using the setter

# Private property using the @property decorator
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public property
        self.__salary = salary  # Private property

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

employee = Employee("Bob Brown", 80000)
# Accessing private property using the @property decorator
print(employee.salary)  # Output: 80000
employee.salary = 90000  # Setting a new salary using the setter