def calculate_carbon_footprint(commute_km, electricity_kwh, meat_meals_per_week):
    """
    Calculates approximate monthly carbon footprint in kg CO2 equivalent.
    """
    commute_monthly = commute_km * 30 * 0.21
    electricity_monthly = electricity_kwh * 0.85
    diet_monthly = meat_meals_per_week * 4 * 7.0
    
    total_footprint = commute_monthly + electricity_monthly + diet_monthly
    return round(total_footprint, 2)

if __name__ == "__main__":
    print("--- Eco-Footprint Calculator (Pre-Fed Values) ---")
    
    # Fixed pre-fed values
    km = 15.0
    kwh = 200.0
    meals = 4.0
    
    print(f"Pre-fed Inputs -> Commute: {km} km/day | Electricity: {kwh} kWh/mo | Meat Meals: {meals}/week")
    
    footprint = calculate_carbon_footprint(km, kwh, meals)
    print(f"Your estimated monthly carbon footprint is {footprint} kg CO2e.")