from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi import APIRouter
from database import create_db_tables

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    create_db_tables()
    yield

app = FastAPI(
    title="Book Management API",
    description="API for managing books, authors, and genres",
    version="1.0.0",
    lifespan=lifespan
)

# app.include_router(books_router, prefix="/books", tags=["Books"])