import pandas as pd

df = pd.read_csv('data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Check for missing values
print("=== MISSING VALUES ===")
print(df.isnull().sum())

# Check for useless columns (same value in every row)
print("\n=== CONSTANT COLUMNS ===")
for col in df.columns:
    if df[col].nunique() == 1:
        print(f"{col}: {df[col].unique()}")

# Drop useless columns
df = df.drop(columns=['EmployeeCount', 'Over18', 'StandardHours'])

# Convert Attrition to numeric (Yes=1, No=0)
df['AttritionNum'] = df['Attrition'].map({'Yes': 1, 'No': 0})

print("\n=== CLEANED SHAPE ===")
print(df.shape)

# Save cleaned data
df.to_csv('data/processed/hr_clean.csv', index=False)
print("Saved: data/processed/hr_clean.csv")