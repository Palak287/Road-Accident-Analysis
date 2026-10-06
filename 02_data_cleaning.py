import pandas as pd

# Load raw dataset
df = pd.read_csv(
    "../road_accidents.csv",
    low_memory=False,
    dtype={"collision_index": "string"}
)

print("===== DATA CLEANING =====")

# Convert date column
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Convert time column
df["time"] = pd.to_datetime(
    df["time"],
    format="%H:%M",
    errors="coerce"
).dt.time

# Remove duplicate rows
df = df.drop_duplicates()

# Check missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("../road_accidents_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Final Shape:", df.shape)