from typing import Optional

from sqlmodel import SQLModel, Field
from datetime import datetime

class Book(SQLModel, table=True):
    __tablename__ = "books"
    id: Optional[int] | None = Field(default=None, primary_key=True)
    title: str
    isbn: str
    publication_year: int

    # Foreign keys to other tables
    user_id: int = Field(None, foreign_key="users.id")
    author_id: int = Field(None, foreign_key="authors.id")
    genre_id: int = Field(None, foreign_key="genres.id")

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)