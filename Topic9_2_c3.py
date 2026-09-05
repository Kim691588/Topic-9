# Topic9_2_c3.py
# Task 3: Search books by author and test using unittest

import sqlite3
import unittest


class BookRepository:
    """Handles all database operations for Book objects."""

    def __init__(self, db_name="library_c3.db"):
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

    def search_by_author(self, author_name):
        self.cursor.execute(
            "SELECT * FROM books WHERE author = ?",
            (author_name,)
        )
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


class TestBookRepository(unittest.TestCase):

    def test_search_by_author_returns_matching_books(self):
        repo = BookRepository(":memory:")

        repo.add_book(1, "Introduction to Python", "J. Smith")

        results = repo.search_by_author("J. Smith")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1], "Introduction to Python")

        repo.close()


if __name__ == "__main__":
    unittest.main()