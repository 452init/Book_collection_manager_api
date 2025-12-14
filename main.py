from os import close
from typing import Union

from fastapi import FastAPI
import sqlite3
import json
app = FastAPI()
@app.post("/books")
def add_new_book():
    return {"Successfully added."}

@app.get("/books")
def fetch_all_books():
    try:
        # connect to books database
        connector = sqlite3.connect("books_database")

        # creates a cursor object
        cursor = connector.cursor()

        # runs a SELECT query
        cursor.execute("SELECT * FROM books_database")

        #Fetch all rows
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        #close connection
        connector.close()

@app.patch("/books/{book_id}")
def update_book():
    return {"Successfully updated."}

@app.delete("/books/{book_id}")
def remove_book():
    return {"Successfully deleted."}