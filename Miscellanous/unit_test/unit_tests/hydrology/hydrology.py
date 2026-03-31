def calculate_discharge(area, velocity):
    """Calculates river discharge in cubic meters per second."""
    if area < 0 or velocity < 0:
        raise ValueError("Physical dimensions cannot be negative")
    
    return area * velocity



