# Basic Inheritance: A class can inherit attributes and methods from another class, allowing for code reuse and the creation of a hierarchy of classes.
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")

class Employee(Person):  # Employee class inherits from Person class
    def __init__(self, name, address, employee_id):
        super().__init__(name, address)  # Call the constructor of the parent class
        self.employee_id = employee_id

employee = Employee("Frank Green", "987 Maple St", "E123")
employee.display_info()  # Output: Name: Frank Green
                         #         Address: 987 Maple St
print(employee.employee_id)  # Output: E123

# Multilevel Inheritance: A class can inherit from another class, which in turn inherits from another class, forming a chain of inheritance.
class Manager(Employee):  # Manager class inherits from Employee class
    def __init__(self, name, address, employee_id, department):
        super().__init__(name, address, employee_id)  # Call the constructor of the parent class
        self.department = department

manager = Manager("Alice Brown", "555 Pine St", "M456", "Sales")
manager.display_info()  # Output: Name: Alice Brown
                        #         Address: 555 Pine St
print(manager.employee_id)  # Output: M456
print(manager.department)  # Output: Sales

# Hierarchical Inheritance: Multiple classes can inherit from a single parent class, allowing for the creation of different subclasses that share common attributes and methods.
class Intern(Person):  # Intern class inherits from Person class
    def __init__(self, name, address, internship_duration):
        super().__init__(name, address)  # Call the constructor of the parent class
        self.internship_duration = internship_duration

intern = Intern("Bob Smith", "123 Oak St", "6 months")
intern.display_info()  # Output: Name: Bob Smith
                        #         Address: 123 Oak St
print(intern.internship_duration)  # Output: 6 months

# Hybrid Inheritance: A combination of two or more types of inheritance, allowing for more complex relationships between classes.
class Contractor(Employee):  # Contractor class inherits from Employee class
    def __init__(self, name, address, employee_id, contract_duration):
        super().__init__(name, address, employee_id)  # Call the constructor of the parent class
        self.contract_duration = contract_duration

contractor = Contractor("Charlie Davis", "789 Elm St", "C789", "12 months")
contractor.display_info()  # Output: Name: Charlie Davis
                             #         Address: 789 Elm St
print(contractor.employee_id)  # Output: C789
print(contractor.contract_duration)  # Output: 12 months    
