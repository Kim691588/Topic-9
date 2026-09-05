# Topic9_4_p.py
# Practical Programming Question:
# Find the most common genre in a book catalogue.

def most_common_genre(catalogue):
    genre_counts = {}

    for book in catalogue:
        for genre in book["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    if not genre_counts:
        return None

    return max(genre_counts, key=genre_counts.get)


catalogue = [
    {"title": "Python Basics", "genres": ["programming", "beginner"]},
    {"title": "Advanced Algorithms", "genres": ["programming", "advanced"]},
    {"title": "Python Projects", "genres": ["programming", "beginner"]},
    {"title": "The Great Journey", "genres": ["fiction", "adventure"]},
]

result = most_common_genre(catalogue)

print("Most common genre:", result)