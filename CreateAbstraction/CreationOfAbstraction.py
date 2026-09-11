# Abstraction in python is a process of hiding the implementation details and showing only functionality to the user. In Python, abstraction can be achieved through abstract classes and interfaces.

class AbstractEmployee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        raise NotImplementedError("Subclasses must implement this method")

class FullTimeEmployee(AbstractEmployee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_details(self):
        return f"Full-Time Employee: {self.name}, Salary: {self.salary}"

class PartTimeEmployee(AbstractEmployee):
    def __init__(self, name, hourly_rate):
        super().__init__(name)
        self.hourly_rate = hourly_rate

    def get_details(self):
        return f"Part-Time Employee: {self.name}, Hourly Rate: {self.hourly_rate}"

# Example usage
full_time_emp = FullTimeEmployee("Alice", 60000)
print(full_time_emp.get_details())  # Output: Full-Time Employee: Alice, Salary:60000
part_time_emp = PartTimeEmployee("Bob", 20)
print(part_time_emp.get_details())  # Output: Part-Time Employee: Bob, Hourly Rate: 20

# Abstact class with abstract method
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    @abstractmethod
    def get_details(self):
        pass

class FullTimeEmployee(AbstractEmployee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Full-Time Employee: {self.name}, Salary: {self.salary}"

class PartTimeEmployee(AbstractEmployee):
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate

    def get_details(self):
        return f"Part-Time Employee: {self.name}, Hourly Rate: {self.hourly_rate}"

# Example usage
full_time_emp = FullTimeEmployee("Alice", 60000)
print(full_time_emp.get_details())  # Output: Full-Time Employee: Alice, Salary: 60000
part_time_emp = PartTimeEmployee("Bob", 20)
print(part_time_emp.get_details())  # Output: Part-Time Employee: Bob, Hourly Rate: 20

