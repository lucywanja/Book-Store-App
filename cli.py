import click
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from model import Book, Category

@click.group()
def cli():
    """Book Store CLI Application"""
    init_db()

@cli.command()
@click.option('--title', prompt='Title', help='The title of the book')
@click.option('--author', prompt='Author', help='The author of the book')
@click.option('--publisher', prompt='Publisher', help='The publisher of the book')
@click.option('--price', prompt='Price', type=float, help='The price of the book')
@click.option('--category', prompt='Category', help='The category of the book')
def add_book(title, author, publisher, price, category):
    """Add a new book"""
    session = SessionLocal()
    category_obj = session.query(Category).filter_by(name=category).first()
    if not category_obj:
        category_obj = Category(name=category)
        session.add(category_obj)
        session.commit()
        session.refresh(category_obj)

    new_book = Book(title=title, author=author, publisher=publisher, price=price, category_id=category_obj.id)
    session.add(new_book)
    session.commit()
    click.echo(f'Book "{title}" added to the store.')

@cli.command()
@click.option('--book-id', prompt='Book ID', type=int, help='The ID of the book to update')
@click.option('--title', prompt='Title', help='The new title of the book')
@click.option('--author', prompt='Author', help='The new author of the book')
@click.option('--publisher', prompt='Publisher', help='The new publisher of the book')
@click.option('--price', prompt='Price', type=float, help='The new price of the book')
@click.option('--category', prompt='Category', help='The new category of the book')
def update_book(book_id, title, author, publisher, price, category):
    """Update a book by ID"""
    session = SessionLocal()
    book = session.query(Book).get(book_id)
    if book:
        category_obj = session.query(Category).filter_by(name=category).first()
        if not category_obj:
            category_obj = Category(name=category)
            session.add(category_obj)
            session.commit()
            session.refresh(category_obj)
        book.title = title
        book.author = author
        book.publisher = publisher
        book.price = price
        book.category_id = category_obj.id
        session.commit()
        click.echo(f'Book with ID {book_id} has been updated.')
    else:
        click.echo(f'Book with ID {book_id} not found.')

@cli.command()
@click.option('--book-id', prompt='Book ID', type=int, help='The ID of the book to delete')
def delete_book(book_id):
    """Delete a book by ID"""
    session = SessionLocal()
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        click.echo(f'Book with ID {book_id} has been deleted.')
    else:
        click.echo(f'Book with ID {book_id} not found.')

@cli.command()
@click.option('--name', prompt='Category Name', help='The name of the category')
def add_category(name):
    """Add a new category"""
    session = SessionLocal()
    new_category = Category(name=name)
    session.add(new_category)
    session.commit()
    click.echo(f'Category "{name}" added to the store.')

@cli.command()
@click.option('--category-id', prompt='Category ID', type=int, help='The ID of the category to update')
@click.option('--name', prompt='Category Name', help='The new name of the category')
def update_category(category_id, name):
    """Update a category by ID"""
    session = SessionLocal()
    category = session.query(Category).get(category_id)
    if category:
        category.name = name
        session.commit()
        click.echo(f'Category with ID {category_id} has been updated.')
    else:
        click.echo(f'Category with ID {category_id} not found.')

@cli.command()
@click.option('--category-id', prompt='Category ID', type=int, help='The ID of the category to delete')
def delete_category(category_id):
    """Delete a category by ID"""
    session = SessionLocal()
    category = session.query(Category).get(category_id)
    if category:
        session.delete(category)
        session.commit()
        click.echo(f'Category with ID {category_id} has been deleted.')
    else:
        click.echo(f'Category with ID {category_id} not found.')

@cli.command()
def list_books():
    """List all books"""
    session = SessionLocal()
    books = session.query(Book).all()
    for book in books:
        click.echo(book)

@cli.command()
@click.option('--category', prompt='Category Name', help='The category to list books for')
def books_by_category(category):
    """List books by category"""
    session = SessionLocal()
    category_obj = session.query(Category).filter_by(name=category).first()
    if category_obj:
        books = session.query(Book).filter_by(category_id=category_obj.id).all()
        for book in books:
            click.echo(book)
    else:
        click.echo(f'Category "{category}" not found.')

@cli.command()
@click.option('--title', prompt='Book Title', help='The title of the book')
def search_books(title):
    """Search books by title"""
    session = SessionLocal()
    books = session.query(Book).filter(Book.title.ilike(f'%{title}%')).all()
    if books:
        for book in books:
            click.echo(book)
    else:
        click.echo(f'No books found with title containing "{title}".')

@cli.command()
def list_categories():
    """List all categories"""
    session = SessionLocal()
    categories = session.query(Category).all()
    for category in categories:
        click.echo(category)

if __name__ == '__main__':
    cli()
