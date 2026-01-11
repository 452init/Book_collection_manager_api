from pydantic import BaseModel
from typing import Optional
from .models import UserRole

class User(BaseModel):
    username: str
    email: str
    full_name: str

class UserCreate(User):
    password: str

class UserResponse(User):
    id: int
    disabled: bool
    role: str
    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None