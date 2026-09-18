from fastapi import FastAPI

from FastAPI_SQLServer.app.routers.employee_router import router


app = FastAPI(
    title="FastAPI SQL Server API",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def root():

    return {
        "message": "FastAPI SQL Server API is running"
    }