from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .schemas import UserCreate, User
from .services import create_user, login_user
from .auth import get_current_user

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate):
    """
    Register a new user

    TODO:
    1. Call create_user service function with user data
    2. Return the created user

    Think: Why use response_model=User? What fields are excluded?
    """
    pass


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login and receive JWT token

    OAuth2PasswordRequestForm expects: username and password fields

    TODO:
    1. Call login_user service with form_data.username and form_data.password
    2. Return the token response

    Think: Why OAuth2PasswordRequestForm instead of custom schema?
    """
    pass


@router.get("/me", response_model=User)
def read_users_me(current_user: str = Depends(get_current_user)):
    """
    Get current user information

    TODO:
    1. This endpoint is automatically protected by Depends(get_current_user)
    2. You have the username from current_user
    3. Fetch and return the full user object (excluding password)

    Think: How does Depends(get_current_user) protect this route?
    """
    pass


# Keep your existing protected route as an example
@router.get("/protected")
def protected_route(current_user: str = Depends(get_current_user)):
    """
    Example protected route
    """
    return {"message": f"Hello {current_user}!"}