import requests
import json
from datetime import datetime

class DataFetcher:
    """
    Fetches weather data from OpenWeatherMap API
    """
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_weather(self, city_name):
        try:
            params = {
                'q': city_name,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            
            data = response.json()
            return {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:
            print(f"Error fetching weather data: {e}")
            return None

if __name__ == "__main__":
    # Example usage (replace with actual API key)
    fetcher = DataFetcher("your_api_key_here")
    weather_data = fetcher.get_weather("London")
    if weather_data:
        print("Weather Data Fetched:")
        print(json.dumps(weather_data, indent=2))