from sqlmodel import SQLModel, Field
from datetime import datetime

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    author: str
    isbn: str
    genre: str
    publication_year: int
    created_at: datetime
    updated_at: datetime