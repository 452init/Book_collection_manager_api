from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from database import get_session
from .models import User
from .schemas import UserCreate, UserResponse, Token
from .services import create_user, login_user
from .dependencies import get_current_user

router = APIRouter(tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(
        user: UserCreate,
        session: Session = Depends(get_session)
):
   return create_user(session, user)

@router.post("/login", response_model=Token)
def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: Session = Depends(get_session)
):
    return login_user(session, form_data.username, form_data.password)

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user