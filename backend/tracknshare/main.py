from fastapi import FastAPI
from dotenv import load_dotenv



# FastAPI instance
app = FastAPI()

# Load environment variables from .env file
load_dotenv()  


@app.get("/")
async def root():
    return {"message": "Hello World, First API"}