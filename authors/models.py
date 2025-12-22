from sqlmodel import SQLModel, Field

class Author(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author_name: str