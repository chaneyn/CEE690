def calculate_area(width, height):
    return width * height**2

# Test 1: Standard positive integers
assert calculate_area(5, 4) == 20, "Should be 20"

# Test 2: Testing with a zero
assert calculate_area(5, 0) == 0, "Should be 0"

# Test 3: Testing floating point numbers
assert calculate_area(2.5, 2) == 5.0, "Should be 5.0"

print("All tests passed!")



