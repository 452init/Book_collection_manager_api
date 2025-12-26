from sqlmodel import SQLModel
from typing import Optional


class BookCore(SQLModel):
    author: str
    isbn: str
    publication_year: int
class BookBase(BookCore):
    title:str
    genre:str
class BookCreate(BookBase):
    pass

class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    genre: Optional[str] = None
    publication_year: Optional[int] = None

class BookResponse(BookBase):
    id: int