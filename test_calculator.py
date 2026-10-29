from carbon_calculator import calculate_carbon_footprint

def test_calculate_carbon_footprint():
    # Test with known values: 10 km commute, 150 kWh electricity, 5 meat meals/week
    # Expected: (10*30*0.21) + (150*0.85) + (5*4*7.0) = 63 + 127.5 + 140 = 330.5
    result = calculate_carbon_footprint(10, 150, 5)
    assert result == 330.5