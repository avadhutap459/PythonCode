# Creation of partial class in Python
# In Python, we can create a partial class by defining a class in multiple parts.

# First part of the class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

# Second part of the class
class Employee:
    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated to: {self.salary}")

# Example usage
employee = Employee("Alice Johnson", 70000)
employee.display_info()  # Output: Employee Name: Alice Johnson, Salary: 70000
employee.update_salary(75000)  # Output: Salary updated to: 75000   

# Getting error in above code because we are defining the class Employee twice. 
# In Python, the second definition will overwrite the first one, 
# so the methods from the first definition will not be available in the second one. 
# To create a partial class, we can use inheritance or mixins instead of redefining the class.

# How to create a partial class using inheritance
class EmployeeBase:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

class Employee(EmployeeBase):
    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated to: {self.salary}")

# Example usage
employee = Employee("Bob Brown", 80000)
employee.display_info()  # Output: Employee Name: Bob Brown, Salary: 80000
employee.update_salary(85000)  # Output: Salary updated to: 85000


