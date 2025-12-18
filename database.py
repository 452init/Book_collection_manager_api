from sqlmodel import create_engine, SQLModel
#from config DATABASE_URL

sqlite_file_name = "books.db"
DATABASE_URL = f"sqlite:///./{sqlite_file_name}"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)