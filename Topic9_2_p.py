# Topic9_2_p.py
# Practical Programming Question:
# Update the availability of a book using a parameterised UPDATE statement.

import sqlite3


class BookRepository:
    """Handles all database operations for Book objects."""

    def __init__(self, db_name="library_p.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                available INTEGER NOT NULL
            )
        """)
        self.connection.commit()

    def add_book(self, book_id, title, author, available=1):
        self.cursor.execute(
            "INSERT OR REPLACE INTO books VALUES (?, ?, ?, ?)",
            (book_id, title, author, available)
        )
        self.connection.commit()

    def get_book_by_id(self, book_id):
        self.cursor.execute(
            "SELECT * FROM books WHERE book_id = ?",
            (book_id,)
        )
        return self.cursor.fetchone()

    def update_availability(self, book_id, available):
        self.cursor.execute(
            "UPDATE books SET available = ? WHERE book_id = ?",
            (available, book_id)
        )
        self.connection.commit()

    def close(self):
        self.connection.close()


# Demonstration
repo = BookRepository(":memory:")

repo.add_book(1, "Introduction to Python", "J. Smith")

print("Before update:")
print(repo.get_book_by_id(1))

repo.update_availability(1, 0)

print("After update:")
print(repo.get_book_by_id(1))

repo.close()