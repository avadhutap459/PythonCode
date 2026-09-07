# Access Specifiers in Python

# Public: Members are accessible from anywhere "name"

print("Public Access Specifier Example:")

class Employee:

    def __init__(self):
        self.name = "Avadhut"
        self.salary = 50000

    def display(self):
        print(self.name)
        print(self.salary)

employee = Employee()
employee.display()  # Output: Avadhut, 50000
        
# Protected: Members are accessible within the class and its subclasses "_name"
print("Protected Access Specifier Example:")
class ProEmployee:
    def __init__(self):
        self.name = "Avadhut"
        self._salary = 70000

    def _calculate_bonus(self):
        return self._salary * 0.10

class SubProEmployee(ProEmployee):
    def display(self):
        print(self.name)
        print(self._salary) # Output: 70000 
        print(self._calculate_bonus()) # Output: 7000.0

employee = ProEmployee()
print(employee.name)  # Output: Avadhut
print(employee._salary)  # Output: 70000
sub_emp = SubProEmployee()
sub_emp.display()  # Output: Avadhut, 70000, 7000
    
# Private: Members are accessible only within the class "__name"
print("Private Access Specifier Example:")
class PrivateEmployee:
    def __init__(self):
        self.name = "Avadhut"
        self.__salary = 90000

    def __calculate_bonus(self):
        return self.__salary * 0.15
    
    def display(self):
        print(self.name)
        print(self.__salary)
        print(self.__calculate_bonus())

emp = PrivateEmployee()
# print(emp.__calculate_bonus())  # This will raise an AttributeError
print(emp.name)  # Output: Avadhut
# print(emp.__salary)  # This will raise an AttributeError
print(emp.display())  # Output: Avadhut, 90000, 13500.0


# Public + Protected + Private Example
class Employee:

    def __init__(self, name, salary, password):

        # Public
        self.name = name

        # Protected
        self._salary = salary

        # Private
        self.__password = password

    # Public method
    def display(self):
        print("Name:", self.name)
        print("Salary:", self._salary)

    # Protected method
    def _calculate_bonus(self):
        return self._salary * 0.10

    # Private method
    def __validate_password(self):
        return self.__password == "12345"
    

employee = Employee("Avadhut", 100000, "12345")

# print(employee.name) & employee.display() are publicly accessible

# print(employee._salary) & print(employee._calculate_bonus()) Technically works, but _ tells other developers: don't access directly, it's meant for internal use within the class or subclasses.

# print(employee.__password) & print(employee.__validate_password())Not directly accessible.