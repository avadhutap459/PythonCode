from fastapi import FastAPI
from CreateMethod.companyRouter import router

app = FastAPI(
    title="User Management API",
    description="My first FastAPI application",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Welcome to FastAPI"
    }
