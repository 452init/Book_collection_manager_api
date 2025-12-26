from sqlmodel import SQLModel



class GenreCore(SQLModel):
    book_genre: str
class GenreBase(GenreCore):
    pass

class GenreCreate(GenreBase):
    pass

class GenreUpdate(SQLModel):
    book_genre: str

class GenreResponse(GenreBase):
    id: int