from fastapi import APIRouter
from fastapi.responses import JSONResponse
from CreateClass.employee import selfEmp,clsEmp

router = APIRouter(
    prefix="/api/employee",
    tags=["Employee"]
)


@router.get("/EmpNameViaSelf")
def get_emp_name_self():
    
    emp = selfEmp()
    message = emp.displayempname("Avadhut")
    
    return JSONResponse(
        status_code=200,
        content={
            "statusCode": 200,
            "message": message
        }
    )

@router.get("/EmpNameViaCls")
def get_emp_name_cls():
    
    message = clsEmp.displayempname("Avadhut")
    
    return JSONResponse(
            status_code=200,
            content={
                "statusCode": 200,
                "message": message
            }
        )

