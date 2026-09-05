
# Topic9_1_p.py
# Practical Activity: Add borrow and return functionality
# to the Library Management System.

class Book:
    """Represents a single book in the library."""

    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        """Mark the book as borrowed."""
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Member:
    """Represents a library member who can borrow books."""

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """Borrow a book if it is available."""
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        """Return a previously borrowed book."""
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")


# Demonstration
book1 = Book(1, "Introduction to Python", "J. Smith")
member1 = Member(101, "Amina Yusuf")

print(book1)

member1.borrow_book(book1)
print(book1)

member1.return_book(book1)
print(book1)

