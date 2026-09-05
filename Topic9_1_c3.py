# Topic9_1_c3.py
# Programming Challenge 3
# Create multiple Book objects from a list of records.

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


def create_books(records):
    books = []

    for record in records:
        book = Book(record[0], record[1], record[2])
        books.append(book)

    return books


# Task 3: Create books from records
records = [
    (1, "Python Basics", "J. Smith"),
    (2, "Data Structures", "R. Lee")
]

books = create_books(records)

for book in books:
    print(book)