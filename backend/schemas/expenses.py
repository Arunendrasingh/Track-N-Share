from pydantic import BaseModel
from datetime import datetime


# All Expense Model goes here
class ExpenseBase(BaseModel):
    description: str
    amount: float

    class Config:
        orm_mode = True


class ExpenseDisplay(BaseModel):
    id: int


class ExpenseCreate(ExpenseBase):
    date: str


class ExpenseUpdate(ExpenseBase):
    pass

# class ExpenseInDBBase(ExpenseBase):
#     id: int

#     class Config:
#         orm_mode = True

# class Expense(ExpenseInDBBase):
#     pass
