import requests


class WeatherService:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_current_temperature(self, latitude, longitude):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=5
        )

        response.raise_for_status()

        temperature = response.json().get(
            "current_weather", {}
        ).get("temperature")

        return temperature


service = WeatherService()

temperature = service.get_current_temperature(-6.20, 106.85)

print(f"Temperature: {temperature} degrees Celsius")

print(
    "The .get() method is more defensive because it returns None "
    "instead of raising a KeyError when expected data is missing."
)