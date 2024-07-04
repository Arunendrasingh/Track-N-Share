from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
from crud import expense
from schemas.expenses import ExpenseBase



# Router
router = APIRouter()



@router.get("/", response_model=list[ExpenseBase])
def get_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db.get_db)):
    expenses = expense.get_expenses(db, skip=skip, limit=limit)
    return expenses