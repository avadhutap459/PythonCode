class Calculator:
    def add(self , a , b , c = 0):
        return a + b + c
    
    def adfar(self, *args):
        return sum(args)
    
c = Calculator()
print(c.add(4,5))
print(c.add(4,5,1))
print(c.adfar(2,5,3,1))


class Employee:
    def work(self):
        print("Employee is working")
        
class Developer(Employee) :
    def work(self):
        print("Developer is working")

class Tester(Employee):
    def work(self):
        super().work()
        print("Tester is working")

d = Developer()
d.work()

e= Employee()
e.work()

t = Tester()
t.work()