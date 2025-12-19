from sqlmodel import SQLModel, Field

class Genre(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str

# @app.put()
# def create_genre(book_id: int):
#     return {"book_id": book_id}
# create_genre(87192)