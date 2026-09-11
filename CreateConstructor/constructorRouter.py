from fastapi import APIRouter
from fastapi.responses import JSONResponse
from CreateConstructor.constructor  import ClsDefaultConstructor, ClsParameterConstructor,ClsCopyConstructor,ClsDestructor

router = APIRouter(
    prefix="/api/constructor",
    tags=["Constructor"]
)


@router.get("/get-default-constructor")
def get_default_constructor():
    
    obj = ClsDefaultConstructor()
    
    return JSONResponse(
        status_code=200,
        content={
            "statusCode": 200,
            "message": obj.message
        }
    )

@router.get("/get-parameter-constructor")
def get_parameter_constructor():
    
    obj = ClsParameterConstructor("Parameterize Constructor")
    
    return JSONResponse(
        status_code=200,
        content={
            "statusCode": 200,
            "message": obj.message
        }
    )

@router.get("/get-copy-constructor")
def get_copy_constructor():
    
    obj = ClsCopyConstructor("Copy Constructor")
    
    new_obj = obj.__copy__()
    
    return JSONResponse(
        status_code=200,
        content={
            "statusCode": 200,
            "message": new_obj.message
        }
    )

@router.get("/get-constructor-overloading")
def get_constructor_overloading():
    
    obj = ClsCopyConstructor("Copy Constructor")
    
    new_obj = obj.__copy__()
    
    return JSONResponse(
        status_code=200,
        content={
            "statusCode": 200,
            "message": new_obj.message
        }
    )

@router.get("/get-destructor")
def get_destructor():
    obj = ClsDestructor("Destructor called")
    
    del obj
    return JSONResponse(
            status_code=200,
            content={
                "statusCode": 200
            }
        )