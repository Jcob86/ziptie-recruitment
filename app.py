from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

import crud
import models
import schema
from database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/authors/", response_model=schema.AuthorResponse, status_code=status.HTTP_201_CREATED)
def create_author(author: schema.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)


@app.post("/books/", response_model=schema.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schema.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@app.get("/authors/{author_id}", response_model=schema.AuthorResponse, status_code=status.HTTP_200_OK)
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author_by_id(db=db, author_id=author_id)
    if author is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return author


@app.delete("/authors/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author_by_id(db=db, author_id=author_id)
    if author is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not founddddd")

    crud.delete_author(db=db, author_id=author_id)
    return None


@app.get("/authors/", response_model=list[schema.AuthorResponse], status_code=status.HTTP_200_OK)
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """If we want to get for ex. users from 10 to 20, jus type http://localhost:8000/authors/?skip=10&limit=10"""
    return crud.get_authors(db=db, skip=skip, limit=limit)
