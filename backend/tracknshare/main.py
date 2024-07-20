from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer

from core.config import settings
from api.api_v1 import api_router

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "23b6acab8ce1648876e6be89fe038f5dbac8adf09886dbe12d7edd8b0d2d82c0"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



app = FastAPI(
    title="TrackNShare",
    description="Effortlessly Track and Share Expenses",
    version="1.0.0",
)

# Include the API router
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
