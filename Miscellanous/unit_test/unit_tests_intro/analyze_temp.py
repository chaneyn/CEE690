def analyze_temp(deg_f):
    # Convert Fahrenheit to Celsius
    deg_c = (deg_f - 32) * 5/9
    
    # Classify based on Celsius value
    if deg_c >= 30:
        category = "Tropical"
    elif deg_c <= 0:
        category = "Arctic"
    else:
        category = "Temperate"
        
    return deg_c, category

# Test 1: Boiling point of water
# We use round() because floating-point math can be imprecise
temp_c, label = analyze_temp(212)
assert round(temp_c, 2) == 100.0, "Boiling point conversion failed"
assert label == "Tropical", "Boiling point should be Tropical"

# Test 2: Freezing point of water (The Boundary of 'Arctic')
temp_c, label = analyze_temp(32)
assert temp_c == 0.0, "Freezing point conversion failed"
assert label == "Arctic", "Freezing point should be classified as Arctic"

# Test 3: A standard temperate day (50°F is 10°C)
temp_c, label = analyze_temp(50)
assert temp_c == 10.0
assert label == "Temperate", "50°F should be Temperate"

# Test 4: Physical impossibility (Absolute Zero)
# -459.67°F is roughly -273.15°C
temp_c, label = analyze_temp(-459.67)
assert temp_c < 0, "Absolute zero must result in a negative Celsius value"
assert label == "Arctic", "Extreme cold must be Arctic"

print("All tests passed!")


