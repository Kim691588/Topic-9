# Topic9_1_d.py
# Purpose: Translate a project proposal into an initial class design
# for a Library Management System.

class Book:
    """Represents a single book record in the library system."""

    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Member:
    """Represents a library member who can borrow books."""

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


# Demonstration: create sample objects
book1 = Book(1, "Introduction to Python", "J. Smith")
member1 = Member(101, "Amina Yusuf")

print(book1)
print(f"Member: {member1.name} (ID: {member1.member_id})")