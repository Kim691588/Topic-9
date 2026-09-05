# Topic9_2_d.py
# Purpose: Demonstrate a DAO class that connects Book data to SQLite.

import sqlite3


class BookRepository:
    """Handles all database operations for Book objects."""

    def __init__(self, db_name="library.db"):
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

    def close(self):
        self.connection.close()


# Demonstration
repo = BookRepository("demo_library.db")

repo.add_book(1, "Introduction to Python", "J. Smith")
repo.add_book(2, "Data Structures in Python", "R. Lee")

for row in repo.get_all_books():
    print(row)

repo.close()