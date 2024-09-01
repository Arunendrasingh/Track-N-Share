from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    amount = Column(Float, index=True)
    date = Column(Date)
    is_updated = Column(Boolean, default=False)
    edited_by = Column(String, nullable=True)
    paid_by_id = Column(Integer, ForeignKey('users.id'))
    paid_by = relationship("User", back_populates="expenses")
#     group_id = Column(Integer, ForeignKey('group.id'))
#     group = relationship("Group", back_populates="expenses")