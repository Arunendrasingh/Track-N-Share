from fastapi import APIRouter
from api.endpoints import expenses, users



# Router
api_router = APIRouter()

api_router.include_router(users.router, prefix="/signup", tags=["Users"])
api_router.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])