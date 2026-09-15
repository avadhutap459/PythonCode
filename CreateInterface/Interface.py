from abc import ABC , abstractmethod
class IEmployee:
    @abstractmethod
    def get_employee_Date(self):
        pass

class IDepartment:
    @abstractmethod
    def get_department_Data(self):
        pass

class Company(IEmployee , IDepartment) :
    def get_employee_Date(self):
        print("This is employee data")
    
    def get_department_Data(self):
        print("This is department data")
        

c = Company()
c.get_department_Data()
c.get_employee_Date()