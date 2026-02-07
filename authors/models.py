from sqlmodel import SQLModel, Field, ForeignKey

class Author(SQLModel, table=True):
    __tablename__ = "authors"

    id: int | None = Field(default=None, primary_key=True)
    author_name: str
    created_by: ForeignKey