class Employee:
    def __init__(self,name):
        self._name = name

class Developer(Employee):
    def __init__(self, name,language):
        super().__init__(name)
        self._Language = language

d = Developer("Avadhut","CSharp")

print(d._name)
print(d._Language)