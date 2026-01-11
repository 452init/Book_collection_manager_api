from sqlmodel import Session, select, func
from fastapi import HTTPException
from .models import User, UserRole, UserCreate


def create_user(session: Session, user: UserCreate):
    # Check if this is the first user
    statement = select(func.count(User.id))
    user_count = session.exec(statement).one()

    is_first_user = (user_count == 0)

    existing_user = get_user_by_username(session, user.username)
    if existing_user:
        raise HTTPException(...)

    hashed_password = get_password_hash(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        disabled=False,
        role=UserRole.ADMIN if is_first_user else UserRole.USER  # ← First user = admin!
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    if is_first_user:
        print(f"🎉 First user '{db_user.username}' created as ADMIN")

    return UserResponse.from_orm(db_user)