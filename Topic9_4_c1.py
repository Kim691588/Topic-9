# Topic9_4_c1.py

class BookRecommender:
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
    {"title": "Mystery Island", "genres": ["fiction", "mystery"]},
]

engine = BookRecommender(catalogue)

recommendations = engine.recommend("fiction")

print("Fiction recommendations:", recommendations)