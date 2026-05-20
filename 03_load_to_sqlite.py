import pandas as pd
import sqlite3

df = pd.read_csv('data/processed/hr_clean.csv')

# Connect to database (creates file if not exists)
conn = sqlite3.connect('data/processed/hr_analytics.db')

# Load dataframe into SQL table
df.to_sql('employees', conn, if_exists='replace', index=False)

print(f"Loaded {len(df)} rows into table 'employees'")
print("Database saved: data/processed/hr_analytics.db")

conn.close()