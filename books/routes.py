from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from . import services,schemas
from database import start_session

router = APIRouter()

@router.post("/", response_model=schemas.BookResponse, status_code=201)
def create_book(
        book_data: schemas.BookCreate,
        session: Session = Depends(start_session)
):
    """create a new book and adds it to the database"""
    return services.create_book(session, book_data)


@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(
        book_id: int,
        session: Session = Depends(start_session)
):
    """queries the required book from the database"""
    book = services.get_book(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Books not found!")
    return book


@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(
        book_id: int,
        book_data: schemas.BookUpdate,
        session: Session = Depends(start_session)
):
    """updates book in the database"""
    updated_book = services.update_book(session, book_id, book_data)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found!")
    return updated_book

@router.delete("/{book_id}", status_code=204,)
def delete_book(
        book_id: int,
        session: Session = Depends(start_session)
):
    """removes book from the database by deletion"""
    deleted_book = services.delete_book(session, book_id)
    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found!")