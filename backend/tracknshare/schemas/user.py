from typing import Union
from pydantic import BaseModel





class User(BaseModel):
    email:str
    first_name: int | None = None
    last_name: int | None = None
    is_active: bool
    is_superuser: bool

class CreateUser(User):
    password: str