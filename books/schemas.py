from sqlmodel import SQLModel
from typing import Optional


class BookCore(SQLModel):
    isbn: str
    publication_year: int
class BookBase(BookCore):
    title:str
class BookCreate(BookBase):
    pass

class BookUpdate(SQLModel):
    title: Optional[str] = None
    isbn: Optional[str] = None
    publication_year: Optional[int] = None

class BookResponse(BookBase):
    id: int