class Employee:
    def display_role(self):
        print("Role For Employee")
        
class Developer(Employee):
    def display_role(self):
        print("Role For Developer")


e = Employee()
d = Developer()

e.display_role()
d.display_role()