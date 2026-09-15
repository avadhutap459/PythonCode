from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class EmployeM(BaseModel):
    EmpId : int
    EmpName : str
    IsActive : bool
    CreateAt : datetime
    
class IEmployee:
    def GetEmployees(self) -> List[EmployeM] :
        pass
    def GetEmployeeById(self,id : int) -> EmployeM:
        pass
    def InsertEmployee(self,employee : EmployeM) -> None:
        pass
    def UpdateEmployee(self,id : int,employee : EmployeM) -> None:
        pass
    
class Employee(IEmployee):
    emps : List[EmployeM]
    
    def __init__(self):
        self.emps = []
    
    def GetEmployees(self) -> List[EmployeM]:
        return self.emps
    
    def GetEmployeeById(self, id : int) -> Optional[EmployeM]:
        for emp in self.emps:
            if emp.EmpId == id:
                return emp
            
        return None
    
    def InsertEmployee(self, employee : EmployeM) -> None:
        if employee is not None :
            self.emps.append(employee)
        
        return None
    
    def UpdateEmployee(self, id : int, employee : EmployeM):
        for idx , e in enumerate(self.emps) :
            if e.EmpId == id:
                self.emps[idx] = employee
                break

class EmployeeService:
    def __init__(self , employee : IEmployee):
        self.employee = employee
        
    
    def returnEmployees(self) -> List[EmployeM]:
        return self.employee.GetEmployees()
     
    def returnEmployeeById(self, empId : int) -> Optional[EmployeM]:
        return self.employee.GetEmployeeById(empId)
    
    def createNewEmployee(self,employee : EmployeM) -> None :
        return self.employee.InsertEmployee(employee)
    
    def updateExitingEmployee(self,empId : int , employee : EmployeM) -> None:
        return self.employee.UpdateEmployee(empId, employee)
    

e = Employee()
eSvc = EmployeeService(e)
empM = EmployeM(
     EmpId=101, EmpName="Avadhut", IsActive=True, CreateAt=datetime.now()
)

eSvc.createNewEmployee(empM)
print("All Employees:", eSvc.returnEmployees())
print("Found Employee:", eSvc.returnEmployeeById(101))
empM1 = EmployeM(
     EmpId=101, EmpName="Avadhut Parab", IsActive=True, CreateAt=datetime.now()
)
eSvc.updateExitingEmployee(101 , empM1)
print("Updated Employee:", eSvc.returnEmployeeById(101))