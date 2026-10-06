import pandas as pd

# Load dataset
df = pd.read_csv(
    "../road_accidents.csv",
    low_memory=False,
    dtype={"collision_index": "string"}
)

print("===== DATASET INSPECTION =====")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFirst 5 Rows:")
print(df.head())

print("\nBasic Statistics:")
print(df.describe(include="all"))