from sqlmodel import create_engine, SQLModel, Field

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    author: str
    isbn: str
    publication_year: int
    genre: str

sqlite_file_name = "books.db"
DATABASE_URL = f"sqlite:///./{sqlite_file_name}"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()