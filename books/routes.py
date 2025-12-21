from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from . import services
from .schemas import BookResponse
from database import start_session

router = APIRouter()

@router.post("/", response_model=BookResponse, status_code=201)
def create_book(
        book_data: BookCreate, title, author, isbn,
        session: Session = Depends(start_session)
):
    """create a new book"""


@router.get("/{book_id}", response_model=BookResponse)
def get_book():

@router.put("/{book_id}", response_model=BookResponse)
def update_book():

@router.delete("/{book_id}", response_model=BookResponse)
def delete_book():