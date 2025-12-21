from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi import APIRouter
from database import create_db_tables

@asynccontextmanager

async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    async def run_database():
        return create_db_tables()

    run_database()
    yield
app = FastAPI(lifespan=lifespan)

@app.get("/books/models")
async def create_book():
    return "Created book"

@app.get("/authors/models")
async def create_author():
    return "Created author"

@app.put("/genres/models")
async def create_genre(book_id: int):
    return {"book_id": book_id}