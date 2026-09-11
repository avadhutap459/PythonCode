# Creation of a class method in Python
class Employee:
    company_name = "ABC Corporation"  # Class variable

    def __init__(self, name, salary):
        self.name = name  # Instance variable
        self.salary = salary  # Instance variable

    @classmethod
    def get_company_name(cls):
        return cls.company_name  # Accessing class variable using cls
    
# Example usage
employee1 = Employee("John Doe", 50000)
print(f"Employee Name: {employee1.name}")  # Output: Employee Name: John Doe
print(f"Employee Salary: {employee1.salary}")  # Output: Employee Salary: 50000
print(f"Company Name: {Employee.get_company_name()}")  # Output: Company Name: ABC Corporation

# Difference between class method and static method and instance method
class Example:
    class_variable = "I am a class variable"

    def __init__(self, value):
        self.instance_variable = value  # Instance variable

    @staticmethod
    def static_method():
        return "I am a static method"

    @classmethod
    def class_method(cls):
        return f"I am a class method. Class variable: {cls.class_variable}"

    def instance_method(self):
        return f"I am an instance method. Instance variable: {self.instance_variable}"

# Example usage
example = Example("I am an instance variable")
print(example.static_method())  # Output: I am a static method
print(example.class_method())   # Output: I am a class method. Class variable: I am a class variable
print(example.instance_method())  # Output: I am an instance method. Instance variable: I am an instance variable

