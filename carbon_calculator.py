def calculate_carbon_footprint(commute_km, electricity_kwh, meat_meals_per_week):
    """
    Calculates approximate monthly carbon footprint in kg CO2 equivalent.
    Factors:
    - Commute: ~0.21 kg CO2 per km (average car)
    - Electricity: ~0.85 kg CO2 per kWh (global average grid factor)
    - Diet: ~7.0 kg CO2 per meat-heavy meal
    """
    commute_monthly = commute_km * 30 * 0.21
    electricity_monthly = electricity_kwh * 0.85
    diet_monthly = meat_meals_per_week * 4 * 7.0
    
    total_footprint = commute_monthly + electricity_monthly + diet_monthly
    return round(total_footprint, 2)

if __name__ == "__main__":
    print("--- Eco-Footprint Calculator ---")
    km = float(input("Enter daily commute distance (km): "))
    kwh = float(input("Enter monthly electricity consumption (kWh): "))
    meals = float(input("Enter meat-based meals per week: "))
    
    footprint = calculate_carbon_footprint(km, kwh, meals)
    print(f"Your estimated monthly carbon footprint is {footprint} kg CO2e.")