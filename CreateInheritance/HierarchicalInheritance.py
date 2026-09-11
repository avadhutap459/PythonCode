class Employee:
    def login(self):
        print("Login By Employee")

class Developer(Employee):
    def write_code(self):
        print("Write Code")

class Tester(Employee):
    def test_code(self):
        print("Tester")


d = Developer()
d.login()
d.write_code()

T = Tester()
T.login()
T.test_code()