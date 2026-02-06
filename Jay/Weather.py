import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(location):
    if not location:
        return "Please specify a city for the weather."

    api_key = os.getenv("weather_api")
    if not api_key:
        return "Weather API key not found. Please set 'weather_api' in your .env file."

    api_key = api_key.strip()

    try:
        result = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        )
        data = result.json()
    except requests.RequestException:
        return "Failed to fetch weather data. Please try again later."

    if data.get("cod") == "404":
        return f"City '{location}' not found. Please check the location."

    description = data["weather"][0]["description"].capitalize()
    feels_like = round(data["main"]["feels_like"])
    temp_max = round(data["main"]["temp_max"])
    temp_min = round(data["main"]["temp_min"])
    city = location.capitalize()

    weather_text = (
        f"Weather in {city}:\n"
        f"- Description: {description}\n"
        f"- Feels like: {feels_like}°C\n"
        f"- High: {temp_max}°C\n"
        f"- Low: {temp_min}°C"
    )

    return weather_text