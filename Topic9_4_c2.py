# Topic9_4_c2.py

class BookRecommender:
    def __init__(self, catalogue):
        self.catalogue = catalogue

    def recommend(self, preferred_genre, top_n=2):
        scored_books = []

        preferred_genre = preferred_genre.lower()

        for book in self.catalogue:
            genres = [genre.lower() for genre in book["genres"]]
            score = genres.count(preferred_genre)

            if score > 0:
                scored_books.append((score, book["title"]))

        scored_books.sort(reverse=True)

        return [title for score, title in scored_books[:top_n]]


catalogue = [
    {"title": "Python Basics", "genres": ["Programming", "beginner"]},
    {"title": "Advanced Algorithms", "genres": ["PROGRAMMING", "advanced"]},
    {"title": "The Great Journey", "genres": ["fiction", "adventure"]},
]

engine = BookRecommender(catalogue)

recommendations = engine.recommend("programming")

print("Case-insensitive recommendations:", recommendations)