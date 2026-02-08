# utils/weather.py
"""
PHASE 3.2B — REAL WEATHER FETCHING
Source: OpenWeatherMap (Current Weather API)

This module fetches REAL temperature and rainfall.
If the API fails, SAFE DEFAULT VALUES are returned
to prevent server crashes (important for deployment).
"""

import requests

API_KEY = "dd3ae4cce36958ac0a5182b8de4bf96e"

def get_weather(city, state):
    """
    Fetch real-time temperature and rainfall for a city.

    Returns:
        temperature (°C)
        rainfall (mm in last 1 hour)
    """

    try:
        location = f"{city},{state},IN"
        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={location}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url, timeout=10)
        data = response.json()

        # --- API FAILURE HANDLING ---
        if response.status_code != 200:
            print("Weather API error:", data.get("message"))
            return 28.0, 100.0   # SAFE DEFAULTS

        # --- TEMPERATURE ---
        temperature = float(data["main"]["temp"])

        # --- RAINFALL ---
        rainfall = 0.0
        if "rain" in data:
            rainfall = float(data["rain"].get("1h", 0.0))

        return round(temperature, 2), round(rainfall, 2)

    except Exception as e:
        # FINAL SAFETY NET (VERY IMPORTANT)
        print("Weather fetch failed:", e)
        return 28.0, 100.0
