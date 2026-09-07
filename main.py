from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    message = "Hello from FastAPI"
    return {
        "message": message
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    name = "Avadhut"
    return {
        "user_id": user_id,
        "name": name
    }
