# Topic9_1_c2.py
# Programming Challenge 2
# Compare two Book objects using their book_id.

class Book:
    """Represents a single book record."""

    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"

    def __eq__(self, other):
        return self.book_id == other.book_id


class Member:
    """Represents a library member."""

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


# Task 2: Create two books with the same ID
book1 = Book(1, "Introduction to Python", "J. Smith")
book2 = Book(1, "Advanced Python", "A. Brown")

print(book1 == book2)