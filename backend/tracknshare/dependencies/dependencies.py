import jwt
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from dependencies.get_db import get_db
from core import security

from api.endpoints.auth import oauth2_scheme
from crud import users


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.exceptions.InvalidTokenError:
        raise credentials_exception
    user = users.get_user(db, username)
    if user is None:
        raise credentials_exception
    return user