class LibrarySystem:
    """Coordinates database, API, and AI components for the library."""

    def __init__(self, repository, weather_service, recommender):
        self.repository = repository
        self.weather_service = weather_service
        self.recommender = recommender

    def daily_briefing(self, latitude, longitude, preferred_genre):
        books = self.repository.get_all_books()

        temperature = self.weather_service.get_current_temperature(
            latitude,
            longitude
        )

        recommendations = self.recommender.recommend(preferred_genre)

        print(f"Books in catalogue: {len(books)}")

        if temperature is not None:
            print(f"Current temperature: {temperature} degrees Celsius")
        else:
            print("Weather data unavailable")

        print(f"Recommended for you: {recommendations}")


class SampleRepository:
    def get_all_books(self):
        return [
            {"title": "Python Basics", "author": "A. Chen"},
            {"title": "Advanced Algorithms", "author": "B. Smith"}
        ]


class SampleWeatherService:
    def get_current_temperature(self, latitude, longitude):
        return 29.4


class SampleRecommender:
    def recommend(self, preferred_genre):
        return ["Python Basics", "Advanced Algorithms"]


if __name__ == "__main__":
    library = LibrarySystem(
        SampleRepository(),
        SampleWeatherService(),
        SampleRecommender()
    )

    library.daily_briefing(
        -9.4438,
        147.1803,
        "programming"
    )