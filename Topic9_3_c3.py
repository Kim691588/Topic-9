import requests


class WeatherService:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_current_weather(self, latitude, longitude):
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
                return None

            return temperature, windspeed

        except requests.exceptions.RequestException:
            return None

    def get_forecast_summary(self, latitude, longitude):
        weather = self.get_current_weather(latitude, longitude)

        if weather is None:
            return "Weather data unavailable"

        temperature, windspeed = weather

        return f"{temperature}°C, wind {windspeed} km/h"


service = WeatherService()

summary = service.get_forecast_summary(-6.20, 106.85)

print(f"Weather summary: {summary}")