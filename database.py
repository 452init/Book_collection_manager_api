from sqlmodel import create_engine, SQLModel

DATABASE_URL = "sqlite:///db.sqlite"

engine = create_engine(DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)