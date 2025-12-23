from sqlmodel import Session
from .models import Author
from . import schemas

def create_author(
        session: Session,
        author_data: schemas.AuthorCreate
):
    author_instance = Author(**author_data.model_dump())
    session.add(author_instance)
    session.commit()
    session.refresh(author_instance)
    return author_instance


def get_author(
        session: Session,
        author_id
):
    author = session.get(Author, author_id)
    if author:
        return author
    else:
        return None

def update_author(
        session: Session,
        author_id,
        author_data: schemas.AuthorUpdate
):
    author = session.get(Author, author_id)
    if not author:
        return None
    else:
        update_data = author_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(author, key, value)
        session.add(author)
        session.commit()
        session.refresh(author)
        return author

def delete_author(
        session: Session,
        author_id
):
    author = session.get(Author, author_id)
    if not author:
        return False
    else:
        session.delete(author)
        session.commit()
        return True