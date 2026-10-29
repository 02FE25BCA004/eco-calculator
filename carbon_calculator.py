import os
import sys

def calculate_carbon_footprint(commute_km, electricity_kwh, meat_meals_per_week):
    commute_monthly = commute_km * 30 * 0.21
    electricity_monthly = electricity_kwh * 0.85
    diet_monthly = meat_meals_per_week * 4 * 7.0
    
    total_footprint = commute_monthly + electricity_monthly + diet_monthly
    return round(total_footprint, 2)

if __name__ == "__main__":
    print("--- Eco-Footprint Calculator ---")
    
    # Check if environment variables are passed via Docker
    if os.getenv("COMMUTE_KM") and os.getenv("ELECTRICITY_KWH") and os.getenv("MEAT_MEALS"):
        km = float(os.getenv("COMMUTE_KM"))
        kwh = float(os.getenv("ELECTRICITY_KWH"))
        meals = float(os.getenv("MEAT_MEALS"))
        print(f"[Environment Mode] Commute: {km}km | Electricity: {kwh}kWh | Meals: {meals}/wk")
    else:
        try:
            km = float(input("Enter daily commute distance (km): "))
            kwh = float(input("Enter monthly electricity consumption (kWh): "))
            meals = float(input("Enter meat-based meals per week: "))
        except (EOFError, KeyboardInterrupt):
            km, kwh, meals = 10.0, 150.0, 5.0
            print(f"\n[Default Mode] Using defaults -> Commute: {km}km, Electricity: {kwh}kWh, Meals: {meals}")

    footprint = calculate_carbon_footprint(km, kwh, meals)
    print(f"Your estimated monthly carbon footprint is {footprint} kg CO2e.")