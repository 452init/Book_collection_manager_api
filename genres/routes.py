from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from . import services,schemas
from database import start_session

router = APIRouter()

@router.post("/", response_model=schemas.GenreResponse, status_code=201)
def create_genre(
        author_data: schemas.GenreCreate,
        session: Session = Depends(start_session)
):
    """create a new book and adds it to the database"""
    return services.create_genre(session, author_data)


@router.get("/{genre_id}", response_model=schemas.GenreResponse)
def get_genre(
        genre_id: int,
        session: Session = Depends(start_session)
):
    """queries the required book from the database"""
    genre = services.get_genre(session, genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found!")
    return genre


@router.put("/{genre_id}", response_model=schemas.GenreResponse)
def update_genre(
        genre_id: int,
        genre_data: schemas.GenreUpdate,
        session: Session = Depends(start_session)
):
    """updates book in the database"""
    updated_genre = services.update_genre(session, genre_id, genre_data)
    if not updated_genre:
        raise HTTPException(status_code=404, detail="Genre not found!")
    return updated_genre

@router.delete("/{genre_id}", status_code=204,)
def delete_genre(
        genre_id: int,
        session: Session = Depends(start_session)
):
    """removes book from the database by deletion"""
    genre = services.delete_genre(session, genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found!")