import requests

try:
    response = requests.get(
        "https://invalid.example.doesnotexist",
        timeout=3
    )
    print(response.status_code)

except requests.exceptions.RequestException:
    print("Request failed")