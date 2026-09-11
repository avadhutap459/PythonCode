class Employee:
    def display_role(self):
        print("Role For Employee")

class Developer(Employee):
    def display_role(self):
        super().display_role()
        print("Role For Developer")
        

d = Developer()
d.display_role()