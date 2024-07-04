from fastapi import APIRouter
from api.endpoints import expenses



# Router
api_router = APIRouter()

api_router.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])