from fastapi import FastAPI
from fastapi import APIRouter
from database import create_db_tables

app = FastAPI()

@app.on_event("startup")
async def run_database():
    return create_db_tables()
@app.get("/books/models")
async def create_book():
    return "Created book"

@app.get("/authors/models")
async def create_author():
    return "Created author"

@app.put("/genres/models")
async def create_genre(book_id: int):
    return {"book_id": book_id}