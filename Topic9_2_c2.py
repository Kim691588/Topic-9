# Topic9_2_c2.py
# Task 2: Delete a book by its ID

import sqlite3


class BookRepository:
    """Handles all database operations for Book objects."""

    def __init__(self, db_name="library_c2.db"):
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

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def delete_book(self, book_id):
        self.cursor.execute(
            "DELETE FROM books WHERE book_id = ?",
            (book_id,)
        )
        self.connection.commit()

    def close(self):
        self.connection.close()


# Demonstration
repo = BookRepository(":memory:")

repo.add_book(1, "Introduction to Python", "J. Smith")
repo.add_book(2, "Data Structures in Python", "R. Lee")

print("Before deletion:")
print(repo.get_all_books())

repo.delete_book(1)

print("After deletion:")
print(repo.get_all_books())

repo.close()