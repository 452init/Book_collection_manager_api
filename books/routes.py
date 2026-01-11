from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from . import services,schemas
from database import get_session
from Authentication.dependencies import get_current_user
from Authentication.permissions import require_active_user
from Authentication.models import User

router = APIRouter()

# PUBLIC - anyone can view books
@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(
        book_id: int,
        session: Session = Depends(get_session)
):
    #queries the required book from the database
    book = services.get_book(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Books not found!")
    return book


# PROTECTED - Must be logged in to create
@router.post("/", response_model=schemas.BookResponse, status_code=201)
def create_book(
        book_data: schemas.BookCreate,
        session: Session = Depends(get_session),
        current_user: User = Depends(require_active_user)
):
    #create a new book and adds it to the database
    return services.create_book(session, book_data, current_user)

# PROTECTED - Must be logged in AND (owner OR admin)
@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(
        book_id: int,
        book_data: schemas.BookUpdate,
        session: Session = Depends(get_session),
        current_user: User = Depends(require_active_user)
):
    #updates book in the database
    return services.update_book(session, book_id, book_data, current_user)


# PROTECTED - Must be logged in AND (owner OR admin)
@router.delete("/{book_id}", status_code=204,)
def delete_book(
        book_id: int,
        session: Session = Depends(get_session),
        current_user: User = Depends(require_active_user)
):
    #removes book from the database by deletion
    deleted_book = services.delete_book(session, book_id, current_user)
    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found!")