import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "../road_accidents_cleaned.csv",
    low_memory=False
)

print("===== ROAD ACCIDENT EDA =====")

# 1. Overall metrics
total_accidents = len(df)
total_casualties = df["number_of_casualties"].sum()
total_vehicles = df["number_of_vehicles"].sum()

print("\n===== OVERALL SUMMARY =====")
print(f"Total Accidents: {total_accidents:,}")
print(f"Total Casualties: {total_casualties:,}")
print(f"Total Vehicles Involved: {total_vehicles:,}")

# 2. Accidents by year
year_analysis = (
    df.groupby("collision_year")
    .size()
    .reset_index(name="Accidents")
    .sort_values("collision_year")
)

print("\n===== ACCIDENTS BY YEAR =====")
print(year_analysis)

# 3. Accident severity
severity_analysis = (
    df.groupby("collision_severity")
    .size()
    .reset_index(name="Accidents")
    .sort_values("Accidents", ascending=False)
)

print("\n===== ACCIDENT SEVERITY =====")
print(severity_analysis)

# 4. Accidents by day of week
day_analysis = (
    df.groupby("day_of_week")
    .size()
    .reset_index(name="Accidents")
    .sort_values("Accidents", ascending=False)
)

print("\n===== ACCIDENTS BY DAY OF WEEK =====")
print(day_analysis)

# 5. Accidents by road type
road_analysis = (
    df.groupby("road_type")
    .size()
    .reset_index(name="Accidents")
    .sort_values("Accidents", ascending=False)
)

print("\n===== ACCIDENTS BY ROAD TYPE =====")
print(road_analysis)

# 6. Accidents by speed limit
speed_analysis = (
    df.groupby("speed_limit")
    .size()
    .reset_index(name="Accidents")
    .sort_values("Accidents", ascending=False)
)

print("\n===== ACCIDENTS BY SPEED LIMIT =====")
print(speed_analysis)

# 7. Urban vs Rural
urban_rural_analysis = (
    df.groupby("urban_or_rural_area")
    .size()
    .reset_index(name="Accidents")
    .sort_values("Accidents", ascending=False)
)

print("\n===== URBAN VS RURAL =====")
print(urban_rural_analysis)

# 8. Weather conditions
weather_analysis = (
    df.groupby("weather_conditions")
    .size()
    .reset_index(name="Accidents")
    .sort_values("Accidents", ascending=False)
)

print("\n===== WEATHER CONDITIONS =====")
print(weather_analysis)

# 9. Light conditions
light_analysis = (
    df.groupby("light_conditions")
    .size()
    .reset_index(name="Accidents")
    .sort_values("Accidents", ascending=False)
)

print("\n===== LIGHT CONDITIONS =====")
print(light_analysis)

# 10. Road surface conditions
surface_analysis = (
    df.groupby("road_surface_conditions")
    .size()
    .reset_index(name="Accidents")
    .sort_values("Accidents", ascending=False)
)

print("\n===== ROAD SURFACE CONDITIONS =====")
print(surface_analysis)

# 11. Monthly accident trend
df["date"] = pd.to_datetime(
    df["date"],
    dayfirst=True,
    errors="coerce"
)

monthly_analysis = (
    df.groupby(df["date"].dt.month)
    .size()
    .reset_index(name="Accidents")
    .rename(columns={"date": "Month"})
)

print("\n===== MONTHLY ACCIDENT TREND =====")
print(monthly_analysis)

# Save analysis files
year_analysis.to_csv("../accidents_by_year.csv", index=False)
severity_analysis.to_csv("../accident_severity_analysis.csv", index=False)
day_analysis.to_csv("../accidents_by_day.csv", index=False)
road_analysis.to_csv("../accidents_by_road_type.csv", index=False)
speed_analysis.to_csv("../accidents_by_speed_limit.csv", index=False)
urban_rural_analysis.to_csv("../urban_rural_analysis.csv", index=False)
weather_analysis.to_csv("../weather_analysis.csv", index=False)
light_analysis.to_csv("../light_conditions_analysis.csv", index=False)
surface_analysis.to_csv("../road_surface_analysis.csv", index=False)
monthly_analysis.to_csv("../monthly_accident_analysis.csv", index=False)

print("\n===== EDA FILES SAVED SUCCESSFULLY =====")
