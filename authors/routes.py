from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from . import services,schemas
from database import start_session

router = APIRouter()

@router.post("/", response_model=schemas.AuthorResponse, status_code=201)
def create_author(
        author_data: schemas.AuthorCreate,
        session: Session = Depends(start_session)
):
    """create a new book and adds it to the database"""
    return services.create_author(session, author_data)


@router.get("/{author_id}", response_model=schemas.AuthorResponse)
def get_author(
        author_id: int,
        session: Session = Depends(start_session)
):
    """queries the required book from the database"""
    author = services.get_author(session, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found!")
    return author


@router.put("/{author_id}", response_model=schemas.AuthorResponse)
def update_author(
        author_id: int,
        author_data: schemas.AuthorUpdate,
        session: Session = Depends(start_session)
):
    """updates book in the database"""
    updated_author = services.update_author(session, author_id, author_data)
    if not updated_author:
        raise HTTPException(status_code=404, detail="Author not found!")
    return updated_author

@router.delete("/{author_id}", status_code=204,)
def delete_author(
        author_id: int,
        session: Session = Depends(start_session)
):
    """removes book from the database by deletion"""
    author = services.delete_author(session, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found!")