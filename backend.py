import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Load from .env file


def get_data(place, days):
    API_KEY = os.getenv("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Same as before
    filtered_data = data["list"]
    nr_values = 8 * days
    return filtered_data[:nr_values]