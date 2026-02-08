from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from . import services,schemas
from database import get_session
from Authentication.permissions import require_admin
from .permissions import require_admin_or_user, Author
from Authentication.models import User

router = APIRouter()

# PUBLIC - Anyone can view authors
@router.get("/{author_id}", response_model=schemas.AuthorResponse)
def get_author(
        author_id: int,
        session: Session = Depends(get_session)
):
    #queries the required author from the database
    author = services.get_author(session, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found!")
    return author

# ADMIN ONLY - Creating authors restricted to admins
@router.post("/", response_model=schemas.AuthorResponse, status_code=201)
def create_author(
        author_data: schemas.AuthorCreate,
        session: Session = Depends(get_session),
        admin_user: User = Depends(require_admin)
):
    #create a new author and adds it to the database
    return services.create_author(session, author_data)

#ADMIN ONLY
@router.put("/{author_id}", response_model=schemas.AuthorResponse)
def update_author(
        author_id: int,
        author_data: schemas.AuthorUpdate,
        verified_author: Author = Depends(require_admin_or_user),
        session: Session = Depends(get_session),
):
    #updates author in the database
    for key, value in author_data.model_dump(exclude_unset=True).items():
        setattr(verified_author, key, value)
    session.add(verified_author)
    session.commit()
    session.refresh(verified_author)
    return verified_author

@router.delete("/{author_id}", status_code=204,)
def delete_author(
        author_id: int,
        session: Session = Depends(get_session),
        admin_user: User = Depends(require_admin)
):
    #removes author from the database by deletion
    author = services.delete_author(session, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found!")