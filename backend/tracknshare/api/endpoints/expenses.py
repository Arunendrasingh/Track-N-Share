from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dependencies import get_db, dependencies
from crud import expense
from schemas.expenses import ExpenseDisplay, ExpenseCreate
from schemas.users import UserInDb

# Router
router = APIRouter()


@router.get("/", response_model=list[ExpenseDisplay])
def get_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db.get_db), user: UserInDb = Depends(dependencies.get_current_user)):
    expenses = expense.get_expenses(db, user.id, skip=skip, limit=limit)
    return expenses


@router.post("add", response_model=ExpenseDisplay, status_code=status.HTTP_201_CREATED)
def add_expense(expense_to_add: ExpenseCreate, db: Session = Depends(get_db.get_db), user: UserInDb = Depends(dependencies.get_current_user)):
    # Add a Creation a message to create a expense.
    new_expense = expense.create(db, obj_in=expense_to_add,paid_by_id=user.id)
    return new_expense

# TODO: Get expense for single user with user id
# TODO: Integrate get_current user log the expense only for specific USER

# TODO: Add a endpoint for updating a expense
