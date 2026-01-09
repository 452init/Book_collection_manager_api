from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI


from Authentication.routes import auth_router
from books.routes import router as books_router
from authors.routes import router as authors_router
from genres.routes import router as genres_router
from database import create_db_tables

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    create_db_tables()
    print("App starting!")
    yield

app = FastAPI(
    title="Book Management API",
    description="API for managing books, authors, and genres",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(books_router, prefix="/books", tags=["Books"])
app.include_router(authors_router, prefix="/authors", tags=["Authors"])
app.include_router(genres_router, prefix="/genres", tags=["Genres"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])