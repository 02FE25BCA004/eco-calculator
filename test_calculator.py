from carbon_calculator import calculate_carbon_footprint

def test_calculate_carbon_footprint():
    # Test using known pre-fed validation numbers
    result = calculate_carbon_footprint(10, 150, 5)
    assert result == 330.5