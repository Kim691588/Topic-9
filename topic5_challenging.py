import unittest


class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_author(self, author):
        return [book for book in self.books if book["author"] == author]


class TestBookRepository(unittest.TestCase):

    def test_search_by_author(self):
        repository = BookRepository()

        repository.add_book({
            "title": "Python Basics",
            "author": "A. Chen"
        })

        repository.add_book({
            "title": "Advanced Python",
            "author": "B. Smith"
        })

        results = repository.search_by_author("A. Chen")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Python Basics")


if __name__ == "__main__":
    unittest.main()