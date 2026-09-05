import unittest


class Book:
    def __init__(self, book_id, title, author, available=True):
        if book_id < 0:
            raise ValueError("Book ID cannot be negative")

        if not title.strip():
            raise ValueError("Title cannot be empty")

        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if not self.available:
            raise Exception("Book is already borrowed")

        self.available = False


class TestBook(unittest.TestCase):

    def test_borrow_changes_availability(self):
        book = Book(1, "Python Essentials", "A. Chen")
        book.borrow()
        self.assertFalse(book.available)

    def test_borrow_already_borrowed_raises_exception(self):
        book = Book(1, "Python Essentials", "A. Chen", available=False)

        with self.assertRaises(Exception):
            book.borrow()

    def test_empty_title_raises_value_error(self):
        with self.assertRaises(ValueError):
            Book(2, "   ", "A. Chen")

    def test_negative_id_raises_value_error(self):
        with self.assertRaises(ValueError):
            Book(-1, "Python Essentials", "A. Chen")


if __name__ == "__main__":
    unittest.main(argv=[""], exit=False)