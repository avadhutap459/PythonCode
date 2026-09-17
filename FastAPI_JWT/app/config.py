import os


SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "development-secret-change-me"
)

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30