from sqlalchemy.orm import Session
from schemas.users import CreateUser
from models.models import User
from passlib.context import CryptContext
from sqlalchemy import select

# Hashed Password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    print("simple Password: ", hashed_password)
    print("Hashed Password: ", plain_password)
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# Add Crud for signUP, SignIn and other details
def create(db: Session, *, obj_in: CreateUser):
    user_save = obj_in.model_dump(exclude_unset=True, exclude_none=True)

    # Pop password1 and password2
    password = user_save.pop("password1")
    user_save.pop("password2")
    user_obj = User(**user_save, hashed_password=get_password_hash(password))
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


def authenticate(db: Session, username: str, password: str):
    user = get_user(db, email=username)
    if not user:
        return False
    
    if not verify_password(password.strip(), user.hashed_password):
        return False
    
    return user
    

