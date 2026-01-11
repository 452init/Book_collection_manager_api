from sqlmodel import Session, select
from fastapi import HTTPException, status
from starlette.status import HTTP_403_FORBIDDEN

from .models import Book
from .schemas import BookCreate, BookResponse, BookUpdate
from Authentication.models import User


def create_book(
        session: Session,
        book_data: BookCreate,
        current_user: User
):
    db_book = Book(
        **book_data.model_dump(),
        user_id=current_user.id
    )
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


def get_book(
        session: Session,
        book_id: int
):
    statement = select(Book).where(Book.id == book_id)
    return session.exec(statement).first()

def update_book(
        session: Session,
        book_id: int,
        book_data: BookUpdate,
        current_user: User
):
    book = get_book(session, book_id)
    if not book:
        raise HTTPException(
            status_code=404, detail="Book not found"
        )

    #Ownership check
    if book.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Not authorized to update this book"
        )

    #Update fields
    for key, value in book_data.model_dump(exclude_unset=True).items():
        setattr(book, key, value)

    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def delete_book(
        session: Session,
        book_id: int,
        current_user: User
):
    book = get_book(session, book_id)
    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    if book.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this book"
        )

    session.delete(book)
    session.commit()
    return True