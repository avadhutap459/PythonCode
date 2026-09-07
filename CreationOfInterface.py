# Creation and implementation of an interface in Python

class EmployeeInterface:
    def get_details(self):
        raise NotImplementedError("Subclasses must implement this method")

class FullTimeEmployee(EmployeeInterface):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Full-Time Employee: {self.name}, Salary: {self.salary}"

# Example usage
full_time_emp = FullTimeEmployee("Alice", 60000)
print(full_time_emp.get_details())  # Output: Full-Time Employee: Alice, Salary: 60000

# Implementation of an interface using the abc module
from abc import ABC, abstractmethod

class EmployeeInterface(ABC):
    @abstractmethod
    def get_details(self):
        pass

class FullTimeEmployee(EmployeeInterface):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Full-Time Employee: {self.name}, Salary: {self.salary}"

# Example usage
full_time_emp = FullTimeEmployee("Alice", 60000)
print(full_time_emp.get_details())  # Output: Full-Time Employee: Alice, Salary: 60000

# Interface segregation principle
class EmployeeInterface(ABC):
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def update_salary(self, new_salary):
        pass

class FullTimeEmployee(EmployeeInterface):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Full-Time Employee: {self.name}, Salary: {self.salary}"

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated to: {self.salary}")

# Example usage
full_time_emp = FullTimeEmployee("Alice", 60000)
print(full_time_emp.get_details())  # Output: Full-Time Employee: Alice, Salary: 60000
full_time_emp.update_salary(65000)  # Output: Salary updated to: 65000

