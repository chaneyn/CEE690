class SoilSensor:
    def __init__(self, location, threshold=20.0):
        self.location = location
        self.threshold = threshold
        self.readings = []

    def add_reading(self, value):
        if value < 0 or value > 100:
            raise ValueError("Moisture percentage must be between 0 and 100")
        self.readings.append(value)

    def needs_water(self):
        if not self.readings:
            return False
        return self.readings[-1] < self.threshold



