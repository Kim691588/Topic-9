# Topic9_1_c1.py
# Programming Challenge 1
# Create and display a Member object.

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


class Member:
    """Represents a library member."""

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


# Task 1: Create a Member object
member2 = Member(102, "David Osei")

print(f"Member: {member2.name} (ID: {member2.member_id})")