from sqlalchemy.orm import Session
from models.expense import Expense
from schemas.expenses import ExpenseCreate, ExpenseUpdate


def get_expense(db: Session, expense_id: int, user_id: int):
    return db.query(Expense).filter(Expense.id == expense_id, Expense.paid_by_id==user_id ).first()


def get_expenses(db: Session, user_id, *, skip=0, limit=100):
    return db.query(Expense).filter(Expense.paid_by_id==user_id).offset(skip).limit(limit).all()



def create(db: Session, *, obj_in: ExpenseCreate, paid_by_id: int):
    db_obj = Expense(
        description=obj_in.description,
        amount=obj_in.amount,
        date=obj_in.date,
        paid_by_id=paid_by_id,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj



class CRUDExpense:
    def get_expense(self, db: Session, expense_id: int, user_id: int):
        return db.query(Expense).filter(Expense.id == expense_id, Expense.paid_by_id == user_id).first()

    def create_expense(self, db: Session, expense: ExpenseCreate, user_id: int):
        db_expense = Expense(**expense.model_dump(), paid_by_id=user_id)
        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)
        return db_expense

    def update_expense(self, db: Session, expense_id: int, user_id: int, expense: ExpenseUpdate):
        db_expense = self.get_expense(db, expense_id, user_id)
        if not db_expense:
            return None
        for key, value in expense.model_dump().items():
            setattr(db_expense, key, value)
        db.commit()
        db.refresh(db_expense)
        return db_expense

    def delete_expense(self, db: Session, expense_id: int, user_id: int):
        db_expense = self.get_expense(db, expense_id, user_id)
        if not db_expense:
            return None
        db.delete(db_expense)
        db.commit()
        return db_expense

    def get_user_expenses(self, db: Session, user_id: int, *, skip=0, limit=100):
        return db.query(Expense).filter(Expense.paid_by_id == user_id).offset(skip).limit(limit).all()

crud_expense = CRUDExpense()