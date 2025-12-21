from sqlmodel import SQLModel
from typing import Optional


class BookBase(SQLModel):
    title: str
    author: str
    isbn: str
    genre: str
    publication_year: int

class BookCreate(BookBase):
        pass

class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    genre: Optional[str] = None
    publication_year: Optional[int] = None

class BookResponse(BookBase):
    id: int