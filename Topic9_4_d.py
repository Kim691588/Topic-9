# Topic9_4_d.py
# Purpose: Demonstrate an AI-style recommendation feature using
# simple keyword matching.

class BookRecommender:
    """Recommends books based on genre keyword similarity."""

    def __init__(self, catalogue):
        self.catalogue = catalogue

    def recommend(self, preferred_genre, top_n=2):
        scored_books = []

        for book in self.catalogue:
            score = book["genres"].count(preferred_genre)

            if score > 0:
                scored_books.append((score, book["title"]))

        scored_books.sort(reverse=True)

        return [title for score, title in scored_books[:top_n]]


catalogue = [
    {"title": "Python Basics", "genres": ["programming", "beginner"]},
    {"title": "Advanced Algorithms", "genres": ["programming", "advanced"]},
    {"title": "The Great Journey", "genres": ["fiction", "adventure"]},
]

engine = BookRecommender(catalogue)

recommendations = engine.recommend("programming")

print("Recommended books:", recommendations)