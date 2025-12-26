from sqlmodel import SQLModel, Field
from datetime import datetime

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    isbn: str
    publication_year: int

    # Foreign keys to other tables
    author_id: int = Field(None, foreign_key="authors.id")
    genre_id: int = Field(None, foreign_key="genres.id")

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)