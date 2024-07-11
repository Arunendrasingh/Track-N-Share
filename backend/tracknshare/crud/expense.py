from sqlalchemy.orm import Session
from tracknshare.db.models import Expense
from tracknshare.schemas.expenses import ExpenseCreate, ExpenseUpdate


def get_expense(db: Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()


def get_expenses(db: Session, *, skip=0, limit=100):
    return db.query(Expense).offset(skip).limit(limit).all()


def create(db: Session, *, obj_in: ExpenseCreate):
    db_obj = Expense(
        description=obj_in.description,
        amount=obj_in.amount,
        date=obj_in.date,
        paid_by_id=obj_in.paid_by_id,
        paid_by=obj_in.paid_by
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
