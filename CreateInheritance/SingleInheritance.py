class company:
    def display(self):
        return "This is super class public method()"
    
class employee(company):
    def display(self):
        print(super().display())
        return "This is derive class public method()"


emp = employee()

print(emp.display())
    
class engine:
    def TwoVehiler(self):
        pass
    def FourVehiler(self):
        pass

class Bike(engine):
    def TwoVehiler(self):
        print("This is 2 ")

class Car(engine):
    def FourVehiler(self):
        print("This is 4")

b = Bike()
b.TwoVehiler();

c = Car()
c.FourVehiler()