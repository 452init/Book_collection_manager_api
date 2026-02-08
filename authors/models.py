from sqlmodel import SQLModel, Field

class Author(SQLModel, table=True):
    __tablename__ = "authors"

    id: int | None = Field(default=None, primary_key=True)
    author_name: str
    created_by: int | None = Field(default=None, foreign_key="users.id")