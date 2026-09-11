class Employee:
    def login(self):
        print("Employee Login")

class Developer(Employee):
    def write_code(self):
        print("Write Code")

class Tester(Employee):
    def test_code(self):
        print("Test Code")

class TeamLead(Developer,Tester):
    def manage_team(self):
        print("Team Management")


TL = TeamLead()
TL.login()
TL.write_code()
TL.test_code()
TL.manage_team()