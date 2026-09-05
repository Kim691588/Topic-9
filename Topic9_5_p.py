import unittest


class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_all_books(self):
        return self.books

    def delete_book(self, book_id):
        self.books = [book for book in self.books if book["id"] != book_id]


class TestBookRepository(unittest.TestCase):

    def test_delete_book_removes_book(self):
        repository = BookRepository()

        repository.add_book({
            "id": 1,
            "title": "Python Basics"
        })

        repository.add_book({
            "id": 2,
            "title": "Advanced Python"
        })

        repository.delete_book(1)

        books = repository.get_all_books()

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["id"], 2)


if __name__ == "__main__":
    unittest.main()