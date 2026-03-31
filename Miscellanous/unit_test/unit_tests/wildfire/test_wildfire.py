import pytest
from wildfire_logic_bugs import calculate_fire_danger

class TestFireDanger:

    def test_high_risk_condition(self):
        # Meets both: low humidity and high wind
        assert calculate_fire_danger(temp=25, humidity=15, wind_speed=35) == "High"

    def test_moderate_risk_temp(self):
        # Only temp is high
        assert calculate_fire_danger(temp=35, humidity=50, wind_speed=10) == "Moderate"

    def test_low_risk_condition(self):
        # Calm, cool, and wet
        assert calculate_fire_danger(temp=15, humidity=60, wind_speed=5) == "Low"

    def test_invalid_humidity_high(self):
        # Testing the upper boundary of humidity
        with pytest.raises(ValueError):
            calculate_fire_danger(20, 105, 10)

    def test_boundary_high_risk(self):
        # Exactly on the wind speed boundary (Rule says > 30)
        # 30 should be Moderate, 31 should be High
        assert calculate_fire_danger(20, 15, 30) == "Moderate"
        assert calculate_fire_danger(20, 15, 31) == "High"
