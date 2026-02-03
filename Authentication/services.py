from sqlmodel import Session, select, func
from .schemas import UserCreate, UserResponse, Token
from .utils import verify_password, get_password_hash, create_access_token
from fastapi import HTTPException, status
from datetime import timedelta
from .models import User, UserRole
from config import ACCESS_TOKEN_EXPIRE_MINUTES

def get_user_by_username(session: Session, username: str):
    statement = select(User).where(User.username == username)
    result = session.exec(statement)
    return result.first()

def create_user(session: Session, user: UserCreate):
    statement = select(func.count(User.id))
    user_count = session.exec(statement).one()
    is_first_user = (user_count == 0)

    if get_user_by_username(session, user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    print(f"Password value: {user.password}")
    print(f"Password type: {type(user.password)}")
    print(f"Password length: {len(str(user.password))}")
    hashed_password = get_password_hash(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        disabled=False,
        role = UserRole.ADMIN if is_first_user else UserRole.USER
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return UserResponse.model_validate(db_user, from_attributes=True)


def authenticate_user(session: Session, username: str, password: str):
    user = get_user_by_username(session, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def login_user(session: Session, username: str, password: str):
    user = authenticate_user(session, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expire
    )

    return Token(access_token=access_token, token_type="bearer")