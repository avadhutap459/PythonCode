from fastapi import APIRouter
from fastapi.responses import JSONResponse
from CreateProperty.property import publicProperty,superClsprotectedProperty,privateProperty,PropertyAttribute

router = APIRouter(
    prefix="/api/company",
    tags=["Company"]
)


@router.get("/get-public-property")
def get_public_property():
    objPro = publicProperty("LargeScale","Vashi","123456","This public property access from anywhere")
    
    return JSONResponse(
        status_code=200,
        content={
            "statusCode": 200,
            "message": objPro.message
        }
    )

@router.get("/get-private-property")
def get_private_property():
    objpri = privateProperty("This is private property")
    
    return JSONResponse(
        status_code=200,
        content={
            "statusCode": 200,
            "message": objpri.returnPrivatePro()
        }
    )

@router.get("/get-protected-property")
def get_protected_property():
    objderiveclass = superClsprotectedProperty("This property access from protected")
    return JSONResponse(
        status_code=200,
        content={
            "statusCode": 200,
            "message": objderiveclass.returnval()
        }
    )
    

@router.get("/get-property-attribute")
def get_property_attribute():
    objpropertyattr = PropertyAttribute()
    return JSONResponse(
        status_code=200,
        content={
            "statusCode": 200,
            "message": objpropertyattr.message
        }
    )