import requests


class WeatherService:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_current_weather(self, latitude, longitude):
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

        weather = response.json()["current_weather"]

        return weather["temperature"], weather["windspeed"]


service = WeatherService()

temperature, windspeed = service.get_current_weather(-6.20, 106.85)

print(f"Temperature: {temperature} degrees Celsius")
print(f"Windspeed: {windspeed} km/h")