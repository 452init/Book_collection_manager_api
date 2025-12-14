from fastapi import FastAPI

from . import services
app = FastAPI()

@router.get("/books/{book_id}")
def is_book_valid(book_id: int):
    for id in book_id:
        return {"book_id": book_id}

@router.post("/books")
def correct_book():
    return {"valid book"}