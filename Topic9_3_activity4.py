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

        data = response.json()

        temperature = data.get("current_weather", {}).get("temperature")

        return temperature


service = WeatherService()

temperature = service.get_current_temperature(-6.20, 106.85)

if temperature is not None:
    print(f"Current temperature: {temperature} degrees Celsius")
else:
    print("Temperature data unavailable")