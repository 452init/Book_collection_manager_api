from sqlmodel import SQLModel, Field

class Genre(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str