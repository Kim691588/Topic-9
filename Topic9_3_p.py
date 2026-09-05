import requests


class NewsHeadlineService:
    def get_status(self, url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.status_code
        except requests.exceptions.RequestException as error:
            print(f"Request failed: {error}")
            return None


service = NewsHeadlineService()

status = service.get_status("https://example.com")

if status is not None:
    print(f"HTTP status: {status}")

failed_status = service.get_status("https://invalid.example.doesnotexist")

print(f"Failed status: {failed_status}")