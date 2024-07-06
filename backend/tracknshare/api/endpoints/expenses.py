from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dependencies.get_db import get_db
from crud import expense
from schemas.expenses import ExpenseBase, ExpenseDisplay, ExpenseCreate



# Router
router = APIRouter()



@router.get("/", response_model=list[ExpenseDisplay])
def get_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    expenses = expense.get_expenses(db, skip=skip, limit=limit)
    return expenses



@router.post("add", response_model=ExpenseDisplay, status_code=status.HTTP_201_CREATED)
def add_expense(expense_to_add: ExpenseCreate, db: Session = Depends(get_db)):
    # Add a Create a message to create a expense..
    new_expense = expense.create(db, obj_in=expense_to_add)
    return new_expense



# TODO: Get single expense for single user with user id

# Add a endpoint for updating a expense