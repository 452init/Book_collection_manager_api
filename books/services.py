from fastapi import FastAPI
import sqlite3
from authors.models import Author, get_author_by_id
app = FastAPI()

def create_book(title, author_id):
    # Validate author exists
    author = get_author_by_id(author_id)
    if not author:
        raise Exception("Author not found")


def get_book_with_author(book_id):
    book = get_book_by_id(book_id)
    author = get_author_by_id(book.author_id)

    return {
        "book": book,
        "author": author
    }


def filter_by_genre():
    pass

def calculate_statistics():
    pass