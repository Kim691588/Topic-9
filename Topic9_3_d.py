# Topic9_3_d.py
# Purpose: Demonstrate an API integration class using a public REST API.

import requests


class WeatherService:
    """Wraps calls to a public weather API (Open-Meteo, no key required)."""

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_current_temperature(self, latitude, longitude):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        }

        try:
            response = requests.get(
                self.BASE_URL,
                params=params,
                timeout=5
            )

            response.raise_for_status()

            data = response.json()

            return data["current_weather"]["temperature"]

        except requests.exceptions.RequestException as error:
            print(f"API request failed: {error}")
            return None


service = WeatherService()

temperature = service.get_current_temperature(-6.20, 106.85)

if temperature is not None:
    print(f"Current temperature: {temperature} degrees Celsius")