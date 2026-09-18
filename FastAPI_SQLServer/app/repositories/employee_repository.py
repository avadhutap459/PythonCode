from sqlalchemy.orm import Session

from FastAPI_SQLServer.app.models.employee import Employee


class EmployeeRepository:

    def __init__(self, db: Session):
        self.db = db


    def get_all(self):

        return (
            self.db
            .query(Employee)
            .all()
        )


    def get_by_id(
        self,
        employee_id: int
    ):

        return (
            self.db
            .query(Employee)
            .filter(
                Employee.EmployeeId == employee_id
            )
            .first()
        )


    def create(
        self,
        employee: Employee
    ):

        self.db.add(employee)

        self.db.commit()

        self.db.refresh(employee)

        return employee


    def delete(
        self,
        employee: Employee
    ):

        self.db.delete(employee)

        self.db.commit()
    
    def update(
        self,
        employee: Employee,
        request
    ):

        employee.EmployeeName = request.EmployeeName
        employee.Department = request.Department
        employee.Salary = request.Salary
        employee.Email = request.Email

        self.db.commit()

        self.db.refresh(employee)

        return employee