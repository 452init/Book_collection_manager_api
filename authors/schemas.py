from sqlmodel import SQLModel



class AuthorCore(SQLModel):
    author_name: str
class AuthorBase(AuthorCore):
    pass

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(SQLModel):
    author_name: str

class AuthorResponse(AuthorBase):
    id: int