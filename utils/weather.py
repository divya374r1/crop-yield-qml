# utils/weather.py
"""
PHASE 3.2B — REAL WEATHER FETCHING
Source: OpenWeatherMap (Current Weather API)

This module fetches REAL temperature and rainfall
for a given district/city using a live weather API.
"""

import requests

API_KEY = "dd3ae4cce36958ac0a5182b8de4bf96e"   # <-- put your key here

def get_weather(city, state):
    """
    Fetch real-time temperature and rainfall for a city.

    Returns:
        temperature (°C)
        rainfall (mm in last 1 hour)
    """

    location = f"{city},{state},IN"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={location}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    # --- ERROR HANDLING ---
    if response.status_code != 200:
        raise ValueError(data.get("message", "Weather API error"))

    # --- TEMPERATURE ---
    temperature = data["main"]["temp"]

    # --- RAINFALL ---
    # Rain may not exist if no rain occurred
    rainfall = 0.0
    if "rain" in data:
        rainfall = data["rain"].get("1h", 0.0)

    return round(temperature, 2), round(rainfall, 2)
