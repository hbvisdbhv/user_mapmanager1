from sqlalchemy import Boolean, Column, ForeignKey,Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    books = relationship("Book",back_populates="author")
    image = Column(String)

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String, index=True)
    description = Column(String)
    image = Column(String)
    pages = Column(Integer)
    author_id = Column(Integer,ForeignKey("authors.id"))
    author = relationship("Author",back_populates="books")


