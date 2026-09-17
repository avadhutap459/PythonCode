from fastapi import (
    APIRouter,
    Depends
)

from FastAPI_JWT.app.auth import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")
async def get_my_profile(
    current_user: dict = Depends(
        get_current_user
    )
):

    return {
        "username":
            current_user["username"],
        "role":
            current_user["role"]
    }