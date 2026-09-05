import requests


class WeatherService:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_forecast_summary(self, latitude, longitude):
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

            weather = response.json().get("current_weather", {})

            temperature = weather.get("temperature")
            windspeed = weather.get("windspeed")

            if temperature is None or windspeed is None:
                return "Weather data unavailable"

            return f"{temperature}°C, wind {windspeed} km/h"

        except requests.exceptions.RequestException as error:
            print(f"API request failed: {error}")
            return "Weather data unavailable"


service = WeatherService()

summary = service.get_forecast_summary(-6.20, 106.85)

print("Weather summary:", summary)