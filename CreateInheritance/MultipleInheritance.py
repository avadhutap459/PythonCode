class Tester:
    def test_code(self):
        print("Test code")

class Developer:
    def write_code(self):
        print("write code")

class TeamLead(Tester,Developer):
    def manage_team(self):
        print("mangement")


TL = TeamLead()
TL.test_code()
TL.write_code()
TL.manage_team()