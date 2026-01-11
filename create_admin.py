from database import get_session
from Authentication.models import User, UserRole
from Authentication.utils import get_password_hash


def create_admin():
    session = next(get_session())

    # Check if admin already exists
    from sqlmodel import select
    statement = select(User).where(User.role == UserRole.ADMIN)
    existing_admin = session.exec(statement).first()

    if existing_admin:
        print(f"Admin already exists: {existing_admin.username}")
        return

    # Create admin user
    admin = User(
        username="admin",
        email="admin@example.com",
        full_name="System Administrator",
        hashed_password=get_password_hash("admin123"),  # TODO: Change this!
        role=UserRole.ADMIN,
        disabled=False
    )

    session.add(admin)
    session.commit()
    session.refresh(admin)

if __name__ == "__main__":
    create_admin()