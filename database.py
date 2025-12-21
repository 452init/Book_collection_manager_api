from sqlmodel import create_engine, SQLModel, Session
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

def start_session():
    with Session(engine) as session:
         yield session

def create_db_tables():
    from books.models import Book
    from authors.models import Author
    from genres.models import Genre

    SQLModel.metadata.create_all(engine)