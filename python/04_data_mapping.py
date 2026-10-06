import pandas as pd

# Load cleaned dataset
df = pd.read_csv(
    "../road_accidents_cleaned.csv",
    low_memory=False
)

print("===== DATA MAPPING =====")

# Collision severity
severity_map = {
    1: "Fatal",
    2: "Serious",
    3: "Slight"
}

df["collision_severity_label"] = df["collision_severity"].map(severity_map)

# Urban / Rural
urban_rural_map = {
    1: "Urban",
    2: "Rural",
    3: "Unallocated",
    -1: "Data missing or out of range"
}

df["urban_rural_label"] = df["urban_or_rural_area"].map(urban_rural_map)

# Speed limit
speed_map = {
    -1: "Data missing or out of range"
}

df["speed_limit_label"] = df["speed_limit"].replace(speed_map)

# Display mapped results
print("\n===== COLLISION SEVERITY =====")
print(df["collision_severity_label"].value_counts())

print("\n===== URBAN VS RURAL =====")
print(df["urban_rural_label"].value_counts())

# Save mapped dataset
df.to_csv("../road_accidents_mapped.csv", index=False)

print("\nMapped dataset saved successfully!")
print("Final Shape:", df.shape)
