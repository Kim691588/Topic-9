import unittest


class Book:
    def __init__(self, title, available=True):
        self.title = title
        self.available = available


class Member:
    def __init__(self):
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False


class TestMember(unittest.TestCase):

    def test_borrow_book_adds_book(self):
        book = Book("Python Essentials")
        member = Member()

        member.borrow_book(book)

        self.assertIn(book, member.borrowed_books)


if __name__ == "__main__":
    unittest.main()