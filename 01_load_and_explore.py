import pandas as pd

df = pd.read_csv('data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Shape and preview
print("=== SHAPE ===")
print(df.shape)

# How many employees left vs stayed?
print("\n=== ATTRITION ===")
print(df['Attrition'].value_counts())
print(df['Attrition'].value_counts(normalize=True).round(2))

# Average salary: left vs stayed
print("\n=== AVERAGE MONTHLY INCOME ===")
print(df.groupby('Attrition')['MonthlyIncome'].mean().round(0))

# Attrition by department
print("\n=== ATTRITION BY DEPARTMENT ===")
print(df.groupby('Department')['Attrition'].value_counts())