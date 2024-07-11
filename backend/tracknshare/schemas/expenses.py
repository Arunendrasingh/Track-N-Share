from pydantic import BaseModel
from datetime import datetime


# All Expense Model goes here
class ExpenseBase(BaseModel):
    description: str
    amount: float
    date: datetime | None = None
    paid_by_id: int
    paid_by: str | None = None


class ExpenseDisplay(BaseModel):
    id: int
    description: str
    amount: float
    date: datetime | None = None
    paid_by_id: int
    paid_by: str | None = None


class ExpenseCreate(ExpenseBase):
    # description: str
    # amount: float
    # date: str
    pass


class ExpenseUpdate(ExpenseBase):
    pass

# class ExpenseInDBBase(ExpenseBase):
#     id: int

#     class Config:
#         orm_mode = True

# class Expense(ExpenseInDBBase):
#     pass
