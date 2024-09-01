from datetime import date
from typing import List

from pydantic import BaseModel


class AuthorCreate(BaseModel):
    name: str
    email: str
    birthdate: date


class BookCreate(BaseModel):
    title: str
    genre: str
    published_date: date
    author_id: int


class BookResponse(BaseModel):
    id: int
    title: str
    genre: str
    published_date: date
    author_id: int

    class Config:
        orm_mode = True


class AuthorResponse(BaseModel):
    id: int
    name: str
    email: str
    birthdate: date
    books: List[BookResponse] = []

    class Config:
        orm_mode = True
