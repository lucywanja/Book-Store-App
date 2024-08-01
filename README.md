# Book Store CLI Application

## Project Description
The Book Store CLI Application is a command-line tool designed to manage a virtual book store. It allows users to create, view, update, and delete book entries as well as manage book categories. The application uses SQLAlchemy ORM to interact with an SQLite database and Click to handle the CLI interface.

## Project MVP (Minimum Viable Product)
### Book Management:
- Create a new book entry with attributes such as title, author, publisher, price, and category.
- List all books with details.
- Update a book by its ID.
- Delete a book by its ID.

### Category Management:
- Create a new category.
- List all categories.
- Update a category by its ID.
- Delete a category by its ID.
- View books by category.

### Search & Filtering:
- Find books by various attributes (e.g., title, author).
- Filter books based on categories.

## Project User Stories
- **As a user, I should be able to create a new book entry:** This allows me to add new books to the store by providing necessary details such as title, author, publisher, price, and category.
- **As a user, I should be able to list all available books:** This enables me to see all the books in the store, along with their details, in a structured format.
- **As a user, I should be able to search for books by title or author:** This helps me quickly find specific books without having to scroll through the entire list.
- **As a user, I should be able to create and manage book categories:** This allows me to organize books into different categories, making it easier to browse and find books.
- **As a user, I should be able to view books by category:** This helps me filter books based on their categories, improving the browsing experience.

## Requirements
### ORM Requirements
- The application must include a database created and modified with Python ORM methods that you write.
- The data model must include at least 2 model classes.
- The data model must include at least 1 one-to-many relationship.
- Property methods should be defined to add appropriate constraints to each model class.
- Each model class should include ORM methods (create, delete, get all, and find by id at minimum).

### CLI Requirements
- The CLI must display menus with which a user may interact.
- The CLI should use loops as needed to keep the user in the application until they choose to exit.
- For EACH class in the data model, the CLI must include options to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
- The CLI should validate user input and object creations/deletions, providing informative errors to the user.
- The project code should follow OOP best practices.
- Pipfile contains all needed dependencies and no unneeded dependencies.
- Imports are used in files only where necessary.
- Project folders, files, and modules should be organized and follow appropriate naming conventions.
- The project should include a README.md that describes the application.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd Book-Store-App

2. Create and activate the virtual environment :

   ```pip install pipenv```
   ```pipenv install```

3. Install the dependencies :
   
   ```pipenv install click sqlalchemy```

4. Initialise the database 

5. Usage:

   ```type python cli.py to see all the commands in the terminal```

   Add a new book:
   ``python cli.py add-book --title "To Kill a Mockingbird" --author "Harper Lee" --publisher "J.B. Lippincott & Co." --price 10.99 --category "Fiction"``

   Update a book by ID:
   ``python cli.py update-book --book-id 1 --title "New Title" --author "New Author" --publisher "New Publisher" --price 20.99 --category "New Category"``

   Delete a book by ID:
   ``python cli.py delete-book --book-id 1``

   List All Books:
   ``python cli.py list-books``

   Add a Category:
   ``python cli.py add-category --name "Fiction"``

   Update a Category by ID:
   ``python cli.py update-category --category-id 1 --name "New Category Name``

   Delete a Category by ID:
   ``python cli.py delete-category --category-id 1``

   List all Categories:
   ``python cli.py list-categories``

   List Books By Category:
   ``python cli.py books-by-category --category "Fiction"``

   Search Books By Title:
   ``python cli.py search-books --title "To Kill a Mockingbird"``

# Liscence
# MIT
``
This `README.md` file provides a comprehensive overview of your project, including descriptions, user stories, requirements, installation instructions, usage examples, and more.
``
# Author

    ```Lucy Wanja Kariuki```


