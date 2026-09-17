from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from fastapi.security import (
    OAuth2PasswordBearer
)

from FastAPI_JWT.app.schemas import (
    LoginRequest,
    TokenResponse
)

from FastAPI_JWT.app.security import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token
)


router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


users = {
    "avadhut": {
        "username": "avadhut",
        "password_hash": hash_password(
            "Password123"
        ),
        "role": "admin"
    }
}


@router.post(
    "/login",
    response_model=TokenResponse
)
async def login(
    request: LoginRequest
):

    user = users.get(
        request.username
    )

    if user is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        request.password,
        user["password_hash"]
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(
        {
            "sub": user["username"],
            "role": user["role"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


async def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    payload = decode_access_token(
        token
    )

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    username = payload.get("sub")

    if username is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = users.get(username)

    if user is None:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user