from database import get_session
from sqlmodel import Session
from fastapi import Depends, HTTPException, status
from models import Author
from Authentication.models import User, UserRole
from Authentication.dependencies import get_current_user

def require_admin_or_user(
        session: Session = Depends(get_session()),
        current_user: User = Depends(get_current_user)
) -> User:
    author = session.get(Author)
    if not author:
        raise HTTPException(
            status_code=404,
            detail="Author not found")
    if not(current_user.role == UserRole.ADMIN or author.created_by == current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized"
        )
    return author