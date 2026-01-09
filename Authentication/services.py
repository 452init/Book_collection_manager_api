from .schemas import UserCreate, UserInDB
from .auth import verify_password, get_password_hash, create_access_token
from fastapi import HTTPException, status
from datetime import timedelta
from config import ACCESS_TOKEN_EXPIRE_MINUTES

# Temporary in-memory storage (you'll replace with database later)
fake_users_db = {}


def get_user(username: str):
    """
    Retrieve user from storage

    TODO:
    1. Check if username exists in fake_users_db
    2. If exists, return UserInDB object created from the stored data
    3. If not, return None

    Think: Later, this will query your actual database
    """
    pass


def create_user(user: UserCreate):
    """
    Register a new user

    TODO:
    1. Check if username already exists (use get_user)
    2. If exists, raise HTTPException with status 400, detail "Username already registered"
    3. Hash the password using get_password_hash
    4. Create a UserInDB object with the hashed password
    5. Store in fake_users_db with username as key
    6. Return the created user (without password!)

    Think: Why return User instead of UserInDB?
    """
    pass


def authenticate_user(username: str, password: str):
    """
    Validate user credentials

    TODO:
    1. Get user using get_user(username)
    2. If user doesn't exist, return False
    3. Verify password using verify_password(password, user.hashed_password)
    4. If password wrong, return False
    5. If everything correct, return the user

    Think: Why return False instead of raising exception?
    """
    pass


def login_user(username: str, password: str):
    """
    Login and generate token

    TODO:
    1. Call authenticate_user(username, password)
    2. If authentication fails, raise HTTPException (401, "Incorrect username or password")
    3. Create access token with timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    4. What data should you pass to create_access_token? (hint: sub claim is standard for username)
    5. Return dict with {"access_token": token, "token_type": "bearer"}

    Think: Why return token_type?
    """
    pass