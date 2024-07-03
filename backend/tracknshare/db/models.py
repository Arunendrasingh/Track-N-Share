from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    # expenses = relationship("Expense", back_populates="paid_by")
    # notifications = relationship("Notification", back_populates="user")
    # groups = relationship("GroupMember", back_populates="user")

# class Expense(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     description = Column(String, index=True)
#     amount = Column(Float, index=True)
#     date = Column(Date)
#     paid_by_id = Column(Integer, ForeignKey('user.id'))
#     paid_by = relationship("User", back_populates="expenses")
#     group_id = Column(Integer, ForeignKey('group.id'))
#     group = relationship("Group", back_populates="expenses")

# class Group(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True, nullable=False)
#     description = Column(String, index=True)
#     members = relationship("GroupMember", back_populates="group")
#     expenses = relationship("Expense", back_populates="group")

# class GroupMember(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     group_id = Column(Integer, ForeignKey('group.id'))
#     user = relationship("User", back_populates="groups")
#     group = relationship("Group", back_populates="members")

# class Notification(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     message = Column(String, index=True)
#     is_read = Column(Boolean, default=False)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship("User", back_populates="notifications")
