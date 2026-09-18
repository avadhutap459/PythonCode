from fastapi import HTTPException

from FastAPI_SQLServer.app.models.employee import Employee
from FastAPI_SQLServer.app.repositories.employee_repository import EmployeeRepository


class EmployeeService:

    def __init__(
        self,
        repository: EmployeeRepository
    ):
        self.repository = repository


    def get_all(self):

        return self.repository.get_all()


    def get_by_id(
        self,
        employee_id: int
    ):

        employee = self.repository.get_by_id(
            employee_id
        )

        if employee is None:

            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        return employee


    def create(self, request):

        employee = Employee(
            EmployeeName=request.EmployeeName,
            Department=request.Department,
            Salary=request.Salary,
            Email=request.Email
        )

        return self.repository.create(employee)


    def delete(
        self,
        employee_id: int
    ):

        employee = self.repository.get_by_id(
            employee_id
        )

        if employee is None:

            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        self.repository.delete(employee)

        return {
            "message": "Employee deleted successfully"
        }
    
    def update(
        self,
        employee_id: int,
        request
    ):

        employee = self.repository.get_by_id(
            employee_id
        )

        if employee is None:

            raise HTTPException(
                status_code=404,
                detail="Employee not found"
            )

        return self.repository.update(
            employee,
            request
        )