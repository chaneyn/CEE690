import pytest
from wildfire_logic_bugs import calculate_fire_danger

class TestFireDanger:

    def test_moderate_risk_temp(self):
        # Only temp is high
        assert calculate_fire_danger(temp=35, humidity=50, wind_speed=10) == "Moderate"

    def test_extreme_value(self):
        with pytest.raises(ValueError):
            calculate_fire_danger(temp=35,humidity=101, wind_speed=10)
        with pytest.raises(ValueError):
            calculate_fire_danger(temp=500,humidity=50, wind_speed=10)

    def test_negative_wind_speed(self):
        with pytest.raises(ValueError):
            calculate_fire_danger(temp=35,humidity=50, wind_speed=-10)



