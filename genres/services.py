from sqlmodel import Session
from .models import Genre
from . import schemas

def create_genre(
        session: Session,
        genre_data: schemas.GenreCreate
):
    genre_instance = Genre(**genre_data.model_dump())
    session.add(genre_instance)
    session.commit()
    session.refresh(genre_instance)
    return genre_instance


def get_genre(
        session: Session,
        genre_id
):
    genre = session.get(Genre, genre_id)
    if genre:
        return genre
    else:
        return None

def update_genre(
        session: Session,
        genre_id,
        genre_data: schemas.GenreUpdate
):
    genre = session.get(Genre, genre_id)
    if not genre:
        return None
    else:
        update_data = genre_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(genre, key, value)
        session.add(genre)
        session.commit()
        session.refresh(genre)
        return genre_data

def delete_genre(
        session: Session,
        genre_id
):
    genre = session.get(Genre, genre_id)
    if not genre:
        return False
    else:
        session.delete(genre)
        session.commit()
        return True