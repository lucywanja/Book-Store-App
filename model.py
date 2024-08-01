from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    books = relationship('Book', back_populates='category', cascade="all, delete-orphan")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name})"

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    category = relationship('Category', back_populates='books')

    def __repr__(self):
        return (f"Book(id={self.id}, title={self.title}, author={self.author}, "
                f"publisher={self.publisher}, price={self.price}, category_id={self.category_id})")
