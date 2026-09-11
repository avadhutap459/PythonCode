class Employee:
    def display_employee(self):
        print("Employee")

class Developer(Employee):
    def write_code(self):
        print("Write code")

class SeniorDeveloper(Developer):
    def design_arch(self):
        print("Design Architecture")


obj = SeniorDeveloper()
obj.design_arch()
obj.write_code()
obj.display_employee()


obj = Developer()
obj.design_arch()
obj.write_code()
obj.display_employee()