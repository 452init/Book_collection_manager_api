from sqlmodel import SQLModel
from typing import Optional


class BookCore(SQLModel):
    isbn: str
    publication_year: int

class BookBase(BookCore):
    title:str

class BookCreate(BookBase):
    author_id: int # User must specify author
    genre_id: int # User must specify genre

class BookUpdate(SQLModel):
    title: Optional[str] = None
    isbn: Optional[str] = None
    publication_year: Optional[int] = None
    author_id: Optional[int] = None # Can update author
    genre_id: Optional[int] = None # Can update genre

class BookResponse(BookBase):
    id: int
    author_id: int
    genre_id: int