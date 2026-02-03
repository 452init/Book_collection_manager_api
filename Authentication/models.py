from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    disabled: bool = Field(default=False)
    role: str = Field(default=UserRole.USER)