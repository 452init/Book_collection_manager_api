from sqlmodel import SQLModel



class GenreCore(SQLModel):
    name: str
class GenreBase(GenreCore):
    pass

class GenreCreate(GenreBase):
    pass

class GenreUpdate(SQLModel):
    name: str

class GenreResponse(GenreBase):
    id: int