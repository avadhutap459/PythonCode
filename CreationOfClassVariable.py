class Employee:
    company_name = "Tech Solutions"  # Class variable
    def __init__(self, name, address):
        self.name = name  # Instance variable
        self.address = address  # Instance variable
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Company: {Employee.company_name}")  # Accessing class variable

employee1 = Employee("David Evans", "111 Birch St")
employee1.display_info()  # Output: Name: David Evans, Address: 111 Birch