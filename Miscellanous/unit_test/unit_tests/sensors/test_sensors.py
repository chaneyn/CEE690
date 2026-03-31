import pytest
from sensors import SoilSensor

class TestSoilSensor:
    
    def test_initialization(self):
        sensor = SoilSensor("Amazon Basin", threshold=15.0)
        assert sensor.location == "Amazon Basin"
        assert sensor.threshold == 15.0
        assert sensor.readings == []

    def test_valid_reading(self):
        sensor = SoilSensor("Sahara")
        sensor.add_reading(45.2)
        assert 45.2 in sensor.readings

    def test_invalid_reading_error(self):
        sensor = SoilSensor("Gobi")
        # This checks that the code correctly "crashes" on bad data
        with pytest.raises(ValueError):
            sensor.add_reading(-5)

    def test_irrigation_logic(self):
        sensor = SoilSensor("Farm A", threshold=25.0)
        
        sensor.add_reading(30.0)
        assert sensor.needs_water() is False
        
        sensor.add_reading(10.0)
        assert sensor.needs_water() is True




