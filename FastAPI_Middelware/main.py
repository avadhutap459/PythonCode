from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def my_middleware(
    request: Request,
    call_next
):

    print("Middleware - Request")
    
    print("Method:", request.method)

    print("URL:", request.url)

    print("Path:", request.url.path)

    response = await call_next(request)

    print("Middleware - Response")

    return response


@app.get("/")
async def home():

    print("Endpoint executed")

    return {
        "message": "Hello"
    }