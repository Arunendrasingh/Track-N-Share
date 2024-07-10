from pydantic import BaseModel, field_validator, model_validator, EmailStr, Field





class User(BaseModel):
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None

    


class CreateUser(User):
    password1: str
    password2: str

    # @model_validator(mode="after")
    def check_password_match(self):

        if not self.password1 and not self.password2:
            raise ValueError("Must Provide Password.")

        if self.password1 != self.password2:
            raise ValueError('passwords do not match')
        
        if len(self.password1) < 8:
            raise ValueError("Your password must be at least 8 characters long.")


class ResponseUser(User):
    id: int
    is_active: bool
    is_superuser: bool



