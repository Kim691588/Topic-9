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

        except requests.exceptions.RequestException as error:
            print(f"API request failed: {error}")
            return None


service = WeatherService()

# Location 1: Jakarta
jakarta_temperature = service.get_current_temperature(-6.20, 106.85)

# Location 2: Port Moresby
port_moresby_temperature = service.get_current_temperature(-9.44, 147.18)

print(f"Jakarta temperature: {jakarta_temperature} degrees Celsius")
print(f"Port Moresby temperature: {port_moresby_temperature} degrees Celsius")