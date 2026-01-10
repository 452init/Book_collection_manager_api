from sentry_sdk.consts import DEFAULT_OPTIONS
from sqlmodel import create_engine, SQLModel, Session
from config import DATABASE_URL
from typing import Annotated
from fastapi import Depends

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
         yield session

# SessionDep = Annotated[Session, Depends(get_session)]

def create_db_tables():
    from books.models import Book
    from authors.models import Author
    from genres.models import Genre
    from Authentication.models import User

    SQLModel.metadata.create_all(engine)