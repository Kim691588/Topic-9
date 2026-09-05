import requests


class WeatherService:
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

            return data.get("current_weather", {}).get("temperature")

        except requests.exceptions.RequestException:
            return None


service = WeatherService()

jakarta = service.get_current_temperature(-6.20, 106.85)
port_moresby = service.get_current_temperature(-9.4438, 147.1803)

print(f"Jakarta temperature: {jakarta} degrees Celsius")
print(f"Port Moresby temperature: {port_moresby} degrees Celsius")