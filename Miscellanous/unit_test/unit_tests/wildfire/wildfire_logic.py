# wildfire_logic.py

def calculate_fire_danger(temp, humidity, wind_speed):
    if not (0 <= humidity <= 100) or wind_speed < 0:
        raise ValueError("Invalid environmental data")

    if humidity < 20 and wind_speed > 30:
        return "High"
    elif temp > 30 or humidity < 30:
        return "Moderate"
    else:
        return "Low"
