from fastapi import APIRouter
from fastapi.responses import JSONResponse
from CreateMethod.company import Company

router = APIRouter(
    prefix="/api/company",
    tags=["Company"]
)


@router.get("/getclassmethodf")
def get_method_access_specfier():
    
    company = Company()
    Instance_message = company.display_company_name_self()
    Class_message = Company.display_company_name_cls()
    Static_message = Company.display_company_name_static()
    
    return JSONResponse(
        status_code=200,
        content={
            "statusCode": 200,
            "message": Instance_message,
            "message 2" : Class_message,
            "message 3" : Static_message
        }
    )
