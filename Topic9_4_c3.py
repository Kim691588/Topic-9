# Topic9_4_c3.py

class BookRecommender:
    def __init__(self, catalogue):
        self.catalogue = catalogue

    def recommend(self, preferred_genre, top_n=2):
        scored_books = []

        preferred_genre = preferred_genre.lower()

        for book in self.catalogue:
            genres = [genre.lower() for genre in book["genres"]]
            title = book["title"].lower()

            score = 0

            # Add one point if the genre matches.
            if preferred_genre in genres:
                score += 1

            # Add one point if the genre appears in the title.
            if preferred_genre in title:
                score += 1

            if score > 0:
                scored_books.append((score, book["title"]))

        scored_books.sort(key=lambda item: (-item[0], item[1]))

        return [title for score, title in scored_books[:top_n]]


catalogue = [
    {"title": "Python Basics", "genres": ["programming", "beginner"]},
    {"title": "Advanced Programming", "genres": ["programming", "advanced"]},
    {"title": "The Great Journey", "genres": ["fiction", "adventure"]},
    {"title": "Programming for Beginners", "genres": ["education"]},
]

engine = BookRecommender(catalogue)

recommendations = engine.recommend("programming")

print("Combined-score recommendations:", recommendations)