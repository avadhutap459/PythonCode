# Creation of Encapsulation in Python
class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for salary
    def get_salary(self):
        return self.__salary

    # Setter method for salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

# Example usage
employee = Employee("John Doe", 50000)
print(employee.get_name())  # Output: John Doe
print(employee.get_salary())  # Output: 50000

employee.set_name("Jane Smith")
employee.set_salary(60000)
print(employee.get_name())  # Output: Jane Smith
print(employee.get_salary())  # Output: 60000

