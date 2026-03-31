import pytest
from hydrology import calculate_discharge

class TestHydrology:

    def test_normal_discharge(self):
        # Testing valid input
        assert calculate_discharge(10, 2) == 20

    def test_negative_area_error(self):
        # This test checks if the function correctly catches bad data
        with pytest.raises(ValueError) as excinfo:
            calculate_discharge(-5, 2)
        
        # Optional: You can even check if the error message is correct
        assert "cannot be negative" in str(excinfo.value)

    def test_negative_velocity_error(self):
        with pytest.raises(ValueError):
            calculate_discharge(10, -1)



