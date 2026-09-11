from fastapi import APIRouter
from fastapi.responses import JSONResponse
from CreateVariable.department import departmentSelf,departmentCls

router = APIRouter(
    prefix="/api/department",
    tags=["Department"]
)


@router.get("/DepartNameViaSelf")
def get_depart_name_self():
    
    department = departmentSelf("Information Tech")
    message = department.displaydepartName()
    
    return JSONResponse(
        status_code=200,
        content={
            "statusCode": 200,
            "message": message
        }
    )

@router.get("/DepartNameViaCls")
def get_depart_name_cls():
    
    message = departmentCls.displaydepartName()
    
    return JSONResponse(
            status_code=200,
            content={
                "statusCode": 200,
                "message": message
            }
        )

