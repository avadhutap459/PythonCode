from fastapi import FastAPI

from FastAPI_JWT.app.auth import (
    router as auth_router
)

from FastAPI_JWT.app.routers.user_router import (
    router as user_router
)


app = FastAPI(
    title="FastAPI JWT Authentication"
)


app.include_router(
    auth_router,
    prefix="/auth"
)

app.include_router(
    user_router
)


@app.get("/")
async def home():

    return {
        "message": "FastAPI JWT application"
    }