from sqlmodel import Session
from .models import Book
from . import schemas

def create_book(
        session: Session,
        book_data: schemas.BookCreate
):
    book_instance = Book(**book_data.model_dump())
    session.add(book_instance)
    session.commit()
    session.refresh(book_instance)
    return book_instance


def get_book(
        session: Session,
        book_id
):
    book = session.get(Book, book_id)
    if book:
        return book
    else:
        return None

def update_book(
        session: Session,
        book_id,
        book_data: schemas.BookUpdate
):
    book = session.get(Book, book_id)
    if not book:
        return None
    else:
        update_data = book_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(book, key, value)
        session.add(book)
        session.commit()
        session.refresh(book)
        return book_data

def delete_book(
        session: Session,
        book_id
):
    book = session.get(Book, book_id)
    if not book:
        return False
    else:
        session.delete(book)
        session.commit()
        return True