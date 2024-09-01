from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    birthdate = Column(Date, nullable=False)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    genre = Column(String(50), nullable=False)
    published_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship("Author", back_populates="books")
