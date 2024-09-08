from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependencies import get_db, dependencies
from crud.expense import crud_expense
from schemas.expenses import ExpenseDisplay, ExpenseCreate, ExpenseUpdate
from schemas.users import UserInDb

# Router
router = APIRouter()


@router.post("/", response_model=ExpenseDisplay, status_code=status.HTTP_201_CREATED)
def create_expense_for_user(expense: ExpenseCreate, db: Session = Depends(get_db.get_db), current_user: UserInDb = Depends(dependencies.get_current_user)):
    return crud_expense.create_expense(db, expense, current_user.id)

@router.get("/", response_model=list[ExpenseDisplay])
def read_user_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db.get_db), current_user: UserInDb = Depends(dependencies.get_current_user)):
    return crud_expense.get_user_expenses(db, current_user.id, skip=skip, limit=limit)

@router.get("/{expense_id}", response_model=ExpenseDisplay)
def read_user_expense(expense_id: int, db: Session = Depends(get_db.get_db), current_user: UserInDb = Depends(dependencies.get_current_user)):
    expense = crud_expense.get_expense(db, expense_id, current_user.id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.put("/{expense_id}", response_model=ExpenseDisplay)
def update_user_expense(expense_id: int, expense: ExpenseUpdate, db: Session = Depends(get_db.get_db), current_user: UserInDb = Depends(dependencies.get_current_user)):
    updated_expense = crud_expense.update_expense(db, expense_id, current_user.id, expense)
    if not updated_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated_expense

@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_expense(expense_id: int, db: Session = Depends(get_db.get_db), current_user: UserInDb = Depends(dependencies.get_current_user)):
    deleted_expense = crud_expense.delete_expense(db, expense_id, current_user.id)
    if not deleted_expense:
        raise HTTPException(status_code=404, detail="Expense not found")


# TODO: Add a endpoint for updating a expense
# TODO: Update the expense in UserProfile when he added the expense,
