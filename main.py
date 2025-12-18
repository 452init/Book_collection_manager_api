from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()

@app.get("/books/models")
def create_book():
    return "Created book"

@app.get("/authors/models")
def create_author():
    return "Created author"

@app.get("/genres/models")
def create_genre():
    return "Created genre"