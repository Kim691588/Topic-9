import unittest

from Topic9_final import (
    LibrarySystem,
    SampleRepository,
    SampleWeatherService,
    SampleRecommender
)


class TestLibrarySystem(unittest.TestCase):

    def test_daily_briefing_runs_without_exception(self):
        library = LibrarySystem(
            SampleRepository(),
            SampleWeatherService(),
            SampleRecommender()
        )

        try:
            library.daily_briefing(
                -9.4438,
                147.1803,
                "programming"
            )
        except Exception as error:
            self.fail(f"daily_briefing raised an exception: {error}")


if __name__ == "__main__":
    unittest.main()