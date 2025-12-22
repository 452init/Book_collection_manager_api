from sqlmodel import SQLModel



class GenreCore(SQLModel):
    name: str
class GenreBase(GenreCore):
    pass

class GenreCreate(GenreBase):
    pass

class GenreUpdate(GenreBase):
    pass

class GenreResponse(GenreBase):
    id: int