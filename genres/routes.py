from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from . import services,schemas
from database import get_session
from Authentication.permissions import require_admin
from Authentication.models import User

router = APIRouter()

@router.get("/{genre_id}", response_model=schemas.GenreResponse)
def get_genre(
        genre_id: int,
        session: Session = Depends(get_session)
):
    #queries the required book genre from the database
    genre = services.get_genre(session, genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found!")
    return genre


# ADMIN ONLY - All modification endpoints
@router.post("/", response_model=schemas.GenreResponse, status_code=201)
def create_genre(
        genre_data: schemas.GenreCreate,
        session: Session = Depends(get_session),
        admin_user: User = Depends(require_admin)
):
    #create a new book genre and adds it to the database
    return services.create_genre(session, genre_data)


@router.put("/{genre_id}", response_model=schemas.GenreResponse)
def update_genre(
        genre_id: int,
        genre_data: schemas.GenreUpdate,
        session: Session = Depends(get_session),
        admin_user: User = Depends(require_admin)
):
    #updates book genre in the database
    updated_genre = services.update_genre(session, genre_id, genre_data)
    if not updated_genre:
        raise HTTPException(status_code=404, detail="Genre not found!")
    return updated_genre

@router.delete("/{genre_id}", status_code=204,)
def delete_genre(
        genre_id: int,
        session: Session = Depends(get_session),
        admin_user: User = Depends(require_admin)
):
    #removes book genre from the database by deletion
    if not services.delete_genre(session, genre_id):
        raise HTTPException(status_code=404, detail="Genre not found!")