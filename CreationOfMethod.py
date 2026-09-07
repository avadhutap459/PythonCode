
# Method inside a class
class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")

employee = Employee("Bob Brown", "321 Pine St")
employee.display_info()  # Output: Name: Bob Brown, Address: 321 Pine St

# Method with parameters
class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def update_address(self, new_address):
        self.address = new_address

employee = Employee("Charlie Davis", "654 Cedar St")
print(f"Before update: {employee.address}")  # Output: Before update: 654 Cedar St
employee.update_address("987 Maple St")
print(f"After update: {employee.address}")  # Output: After update: 987 Maple St
