from utils.weather import get_weather

temperature, rainfall = get_weather("Bengaluru", "Karnataka")

print("Temperature:", temperature, "°C")
print("Rainfall:", rainfall, "mm")
