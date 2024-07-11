from fastapi import FastAPI
from dotenv import load_dotenv

from core.config import settings
from api.api_v1 import api_router

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
