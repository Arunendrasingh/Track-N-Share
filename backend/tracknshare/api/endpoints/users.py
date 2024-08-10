from fastapi import APIRouter, Depends, status, Body, HTTPException
from sqlalchemy.orm import Session

from dependencies.get_db import get_db
from crud import users
from schemas.users import ResponseUser, CreateUser



# Router
router = APIRouter()



@router.post("/", response_model=ResponseUser, status_code=status.HTTP_201_CREATED)
def signup(user_to_add: CreateUser, db: Session = Depends(get_db)):

    # Check for existing user
    user = users.get_user(db, email=user_to_add.email)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered.")
    
    return users.create(db, obj_in=user_to_add)

    




# TODO: Add other Method like, Profile, UserUpdate, ProfileUpdate.
# TODO: Add Method to increase the total expense, every-time a user add new expense.