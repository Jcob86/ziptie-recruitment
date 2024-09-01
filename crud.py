from sqlalchemy.orm import Session

import models
import schema


def create_author(db: Session, author: schema.AuthorCreate):
    db_author = models.Author(name=author.name, email=author.email, birthdate=author.birthdate)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def create_book(db: Session, book: schema.BookCreate):
    db_book = models.Book(title=book.title, genre=book.genre, published_date=book.published_date, author_id=book.author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_author_by_id(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def delete_author(db: Session, author_id: int):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if author:
        db.delete(author)
        db.commit()


def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()
